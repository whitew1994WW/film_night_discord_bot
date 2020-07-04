from commands.base_command import BaseCommand
import settings
import os
import json


class GetFilm(BaseCommand):

    def __init__(self):
        description = "Returns the current film details"
        params = []
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        super().__init__(description, params)

    async def handle(self, params, message, client):
        film_deets = self.get_film_deets()
        msg = "{role} \n\nWith or without you we will be watching {film_name} on {film_date} at {film_time}.\n " \
              "You might be able to find the film here:\n {film_magnet}".format(role=settings.AUDIENCE, **film_deets)
        await message.channel.send(msg)

    def get_film_deets(self):
        with open(self.save_dict_location) as f:
            film_deets = json.load(f)
        return film_deets
