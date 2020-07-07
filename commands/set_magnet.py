import io
import json
import os

import settings
from commands.base_command import BaseCommand


class SetMagnet(BaseCommand):
    def __init__(self):
        description = "Updates the magnet of the film"
        params = ['new_magnet_link']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        film_deets = self.set_magnet(params[0])
        msg = "{role} \n\nLink has been added for {film_name}:\n " \
              "```{film_magnet}```".format(role=settings.AUDIENCE, **film_deets)
        await message.channel.send(msg)

    def get_film_deets(self):
        with open(self.save_dict_location) as f:
            film_deets = json.load(f)
        return film_deets

    def set_magnet(self, new_magnet):
        film_deets = self.get_film_deets()
        film_deets['film_magnet'] = new_magnet
        with io.open(self.save_dict_location, 'w') as f:
            f.write(json.dumps(film_deets))
        return film_deets
