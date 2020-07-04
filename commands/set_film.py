import io
import json
import os
from datetime import datetime

import settings
from commands.base_command import BaseCommand



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

        with io.open(self.save_dict_location, 'w') as f:
            f.write(json.dumps(film_details))
        return "{role} \n\n{film_name} is scheduled {film_date} at {film_time}.\n " \
               "You might be able to find the film here:\n {film_magnet}".format(role=settings.AUDIENCE, **film_details)

    def embed_gen(self, params):

        # Open the prebuilt embedding jsons and set the user inputs to a the dic
        with open(self.save_embdict_location, 'r') as f:
            embed_dic = json.load(f)
        # Title
        embed_dic["title"] = str(params[0])
        # Time and Date
        embed_dic["fields"][0]["value"] = "{} - {}".format(str(params[2]), str(params[1]))
        # Write the dic back to json file
        with open(self.save_embdict_location, 'w') as f:
            f.write(json.dumps(embed_dic))

