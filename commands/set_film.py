import io
import json
import os
import requests
from datetime import datetime

import settings
from commands.base_command import BaseCommand

KEY = 'a445191a'
INFO_URL = 'http://www.omdbapi.com/?t={movie}&apikey={key}&'

class SetFilm(BaseCommand):
    def __init__(self):
        description = "Sets the details for the upcoming movie night"
        params = ["Film Name", "Film date", "Film current Time", 'Film magnet']
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        self.save_embdict_location = os.path.join(settings.BASE_DIR, 'data', 'embed_file.json')
        super().__init__(description, params)

    async def handle(self, params, message, client):

        self.embed_gen(params)

        msg = self.store_films(params)

        await message.channel.send(msg)

    def store_films(self, params):

        film_details = {'film_name': str(params[0]), 'film_magnet': str(params[3])}
        print(params)
        try:
            datetime.strptime(params[1], "%d/%m/%Y")

        except ValueError:
            return "Please provide the date in the format 'DD/MM/YYYY'"
        film_details['film_date'] = params[1]
        try:
            datetime.strptime(params[2], "%I:%M %p %Z")
        except ValueError:
            return "Please provide the time in the format '1:00 PM GMT'"
        film_details['film_time'] = params[2]

        with open(self.save_dict_location, 'w') as f:
            f.write(json.dumps(film_details))
        return "{role} \n\n{film_name} is scheduled for {film_date} at {film_time}".format(role=settings.AUDIENCE, **film_details)

    def embed_gen(self, params):
        # Pull film data from OMDb
        OMDb_data = self.get_OMDb_data(params[0].replace(" ","+"))

        # Open the prebuilt embedding jsons and set the user inputs to a the dic
        with open(self.save_embdict_location, 'r') as f:
            embed_dic = json.load(f)
        # Title
        embed_dic["title"] = str(params[0])
        # url
        embed_dic["url"] = "https://www.imdb.com/title/{}/".format(OMDb_data["imdbID"])
        # Year, Director and Summary
        embed_dic["description"] = "**{}**\n\n{}\n\n*Director: {}*\n".format(OMDb_data["Year"],OMDb_data["Plot"],OMDb_data["Director"])
        # Ratings
        for i in range(2):
            embed_dic["fields"][i]["value"] = OMDb_data["Ratings"][i]["Value"]
        # Time and Date
        embed_dic["fields"][2]["value"] = "{} - {}".format(str(params[2]), str(params[1]))
        # Image
        embed_dic["image"]["url"] = OMDb_data["Poster"]
        # Write the dic back to json file
        with open(self.save_embdict_location, 'w') as f:
            f.write(json.dumps(embed_dic, indent= 2))

    # API Request from OMDb
    def get_OMDb_data(self,film):

        def get_json(url):
            r = requests.get(url)
            return r.json()

        return get_json(INFO_URL.format(movie=film,key=KEY))