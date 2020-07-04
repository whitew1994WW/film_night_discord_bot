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
        super().__init__(description, params)

    async def handle(self, params, message, client):
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
        return "{role} \n\nWith or without you we will be watching {film_name} on {film_date} at {film_time}.\n " \
               "You might be able to find the film here:\n {film_magnet}".format(role=settings.AUDIENCE, **film_details)
