import io
import json
import os
from datetime import datetime

import settings
from commands.base_command import BaseCommand


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class SetFilm(BaseCommand):
    def __init__(self):
        # A quick description for the help message
        description = "Sets the details for the upcoming movie night"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["Film Name", "Film date", "Film current Time", 'Film magnet']
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object
        msg = self.store_films(params)

        await client.send_message(message.channel, msg)

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
