import io
import json
import os
from datetime import datetime

import settings
from commands.base_command import BaseCommand


class SetTime(BaseCommand):
    def __init__(self):
        description = "Updates the time of the film"
        params = ['new_time']
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        super().__init__(description, params)

    async def handle(self, params, message, client):

        film_deets = self.set_time(params[0])
        msg = "{role} \n\n{film_name} has been set for {film_date}" \
              "at {film_time}.\n ".format(role=settings.AUDIENCE, **film_deets)
        await message.channel.send(msg)

    def set_time(self, new_time):
        info = self.get_info()
        embed_dic = self.get_embed()
        try:
            datetime.strptime(new_time, "%I:%M %p %Z")
        except ValueError:
            return "Please provide the time in the format '1:00 PM GMT'"
        film_deets['film_time'] = new_time
        with io.open(self.save_dict_location, 'w') as f:
            f.write(json.dumps(film_deets))
        return film_deets
