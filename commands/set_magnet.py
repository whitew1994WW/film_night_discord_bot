import io
import json
import os

import settings
from commands.base_command import BaseCommand


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase


# So, a command class named Random will generate a 'random' command
class SetMagnet(BaseCommand):
    def __init__(self):
        # A quick description for the help message
        description = "Updates the magnet of the film"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        params = ['new_magnet_link']
        # If no params are expected, leave this list empty or set it to None
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

        film_deets = self.set_magnet(params[0])
        msg = "{role} \n\nLink has been added for {film_name}:\n " \
              "```{film_magnet}```".format(role=settings.AUDIENCE, **film_deets)
        await client.send_message(message.channel, msg)

    def get_film_deets(self):
        with open(self.save_dict_location) as f:
            film_deets = json.load(f)
        return film_deets

    def set_magnet(self, new_magnet):
        film_deets = self.get_film_deets()
        film_deets['film_magnet'] = new_magnet
        with io.open(self.save_dict_location, 'w') as f:
            f.write(json.dumps(film_deets))
        return film_deets
