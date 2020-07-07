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
        new_time = ' '.join(params)
        msg = self.set_time(new_time)
        await message.channel.send(msg)

    def set_time(self, new_time):

        info = self.get_info()
        embed_dic = self.get_embed()

        info['film_time'] = new_time

        try:
            date = info['film_date']
        except KeyError:
            date = '*No date set*'

        embed_dic["fields"][2]["value"] = "{} - {}".format(new_time, date)

        self.set_info(info)
        self.set_embed(embed_dic)

        return 'Film is scheduled for {}'.format(new_time)