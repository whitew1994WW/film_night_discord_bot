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
        params = ['Film Name']
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        self.save_embdict_location = os.path.join(settings.BASE_DIR, 'data', 'embed_file.json')
        super().__init__(description, params)

    async def handle(self, params, message, client):
        film = ' '.join(params).title()
        nofilm = self.embed_gen(film)
        if not nofilm:
            msg = self.store_films(film)
        else:
            msg = '{}'.format(nofilm)
        await message.channel.send(msg)

    def store_films(self, film):

        info = self.get_info()
        info['film_name'] = film
        self.set_info(info)

        return "{} \n\nNext film is set to {}".format(settings.AUDIENCE, film)

    def embed_gen(self, film):
        # Pull film data from OMDb
        OMDb_data = self.get_OMDb_data(film)
        if 'Error' in OMDb_data:
            return OMDb_data['Error']
        embed_dic = self.get_embed()
        # Title
        embed_dic["title"] = film
        # URL
        embed_dic["url"] = "https://www.imdb.com/title/{}/".format(OMDb_data["imdbID"])
        # Year, Director and Summary
        embed_dic["description"] = "**{}**\n\n{}\n\n*Director: {}*\n".format(OMDb_data["Year"], OMDb_data["Plot"], OMDb_data["Director"])
        # Ratings
        # IMDb
        try:
            embed_dic["fields"][0]["value"] = OMDb_data["Ratings"][0]["Value"]
        except IndexError:
            embed_dic["fields"][0]["value"] = "No Rating"
        # RT
        try:
            embed_dic["fields"][1]["value"] = OMDb_data["Ratings"][1]["Value"]
        except IndexError:
            embed_dic["fields"][1]["value"] = "No Rating"
        # Image
        embed_dic["image"]["url"] = OMDb_data["Poster"]

        self.set_embed(embed_dic)

    # API Request from OMDb
    def get_OMDb_data(self, film):
        r = requests.get(INFO_URL.format(movie=film, key=KEY)).json()
        return r
