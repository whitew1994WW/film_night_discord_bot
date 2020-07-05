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

        info = self.set_date(params[0])
        msg = "{role} \n\n{name} has been set for {date}" \
              "at {time}.\n ".format(role=settings.MOVIE_NIGHT_ROLE, **info)
        await message.channel.send(msg)

    def get_info(self):
        with open(self.save_dict_location) as f:
            info = json.load(f)
        return info

    def set_date(self, new_date):
        info = self.get_info()
        try:
            datetime.strptime(new_date, "%d/%m/%Y")
        except ValueError:
            return "Please provide the date in the format 'DD/MM/YYYY'"

        info['date'] = new_date
        with io.open(self.save_dict_location, 'w') as f:
            f.write(json.dumps(info))
        return info
