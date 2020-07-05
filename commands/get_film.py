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
        info = self.get_info()
        msg = "{role} \n\nWith or without you we will be watching {name} on {date} at {time}.\n " \
              "You might be able to find the film here:\n {magnet}".format(role=settings.MOVIE_NIGHT_ROLE, **info)
        await message.channel.send(msg)

    def get_info(self):
        with open(self.save_dict_location) as f:
            info = json.load(f)
        return info
