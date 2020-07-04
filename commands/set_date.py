from commands.base_command import BaseCommand
import settings
import os, io
import json
from datetime import datetime


class SetDate(BaseCommand):
    def __init__(self):
        description = "Updates the date of the film"
        params = ['new_date']
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        super().__init__(description, params)

    async def handle(self, params, message, client):

        film_deets = self.set_date(params[0])
        msg = "{role} \n\n{film_name} has been set for {film_date}" \
              "at {film_time}.\n ".format(role=settings.AUDIENCE, **film_deets)
        await message.channel.send(msg)

    def get_film_deets(self):
        with open(self.save_dict_location) as f:
            film_deets = json.load(f)
        return film_deets

    def set_date(self, new_date):
        film_deets = self.get_film_deets()
        try:
            datetime.strptime(new_date, "%d/%m/%Y")
        except ValueError:
            return "Please provide the date in the format 'DD/MM/YYYY'"

        film_deets['film_date'] = new_date
        with io.open(self.save_dict_location, 'w') as f:
            f.write(json.dumps(film_deets))
        return film_deets
