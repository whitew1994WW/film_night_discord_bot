from commands.base_command import BaseCommand
import settings
import os
import json


class GetFilm(BaseCommand):

    def __init__(self):
        description = "Returns the current film details"
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):
        info = self.get_info()
        msg = "{role} \n\nWith or without you we will be watching {name} on {date} at {time}.\n " \
              "You might be able to find the film here:\n {magnet}".format(role=settings.MOVIE_NIGHT_ROLE, **info)
        await message.channel.send(msg)
