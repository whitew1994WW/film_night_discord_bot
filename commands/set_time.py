from datetime import datetime

import settings
from commands.base_command import BaseCommand


class SetTime(BaseCommand):
    def __init__(self):
        description = "Updates the time of the film"
        params = ['new_time']
        super().__init__(description, params)

    async def handle(self, params, message, client):

        info = self.set_time(params[0])
        msg = "{role} \n\n{name} has been set for {date}" \
              "at {time}.\n ".format(role=settings.MOVIE_NIGHT_ROLE, **info)
        await message.channel.send(msg)

    def set_time(self, new_time):
        info = self.get_info()
        try:
            datetime.strptime(new_time, "%I:%M %p %Z")
        except ValueError:
            return "Please provide the time in the format '1:00 PM GMT'"
        info['time'] = new_time
        self.set_info(info)
        return info
