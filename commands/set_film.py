from datetime import datetime

import settings
from commands.base_command import BaseCommand


class SetFilm(BaseCommand):
    def __init__(self):
        description = "Sets the details for the upcoming movie night"
        params = ["Film Name", "Film date", "Film current Time", 'Film magnet']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        msg = self.store_films(params)

        await message.channel.send(msg)

    def store_films(self, params):
        # TODO only require a film name to initialise a movie night
        info = {'name': str(params[0]), 'magnet': str(params[3]), 'audience': []}
        print(params)
        try:
            datetime.strptime(params[1], "%d/%m/%Y")

        except ValueError:
            return "Please provide the date in the format 'DD/MM/YYYY'"
        info['date'] = params[1]
        try:
            datetime.strptime(params[2], "%I:%M %p %Z")
        except ValueError:
            return "Please provide the time in the format '1:00 PM GMT'"
        info['time'] = params[2]

        self.set_info(info)

        return "{role} \n\nWith or without you we will be watching {name} on {date} at {time}.\n " \
               "You might be able to find the film here:\n {magnet}".format(role=settings.MOVIE_NIGHT_ROLE, **info)
