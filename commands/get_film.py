from commands.base_command  import BaseCommand
import settings
import os
import json

# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class GetFilm(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Returns the current film details"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        params = []
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

        film_deets = self.get_film_deets()
        msg = "With or without you we will be watching {film_name} on {film_date} at {film_time}. " \
              "You might be able to find the film here:\n {film_magnet}".format(**film_deets)
        await client.send_message(message.channel, msg)

    def get_film_deets(self):
        with open(self.save_dict_location) as f:
            film_deets = json.load(f)
        return film_deets