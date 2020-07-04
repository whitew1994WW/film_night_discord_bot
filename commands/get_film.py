from commands.base_command import BaseCommand
import settings
import os
import json
import discord


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
        self.save_embdict_location = os.path.join(settings.BASE_DIR, 'data', 'embed_file.json')
        self.save_magnet_location = os.path.join(settings.BASE_DIR, 'data', 'magnet.json')
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        # bot reply
        embedded_messages = self.get_film_info()
        # sends film info and magnet link
        for emb_mes in embedded_messages:
            await message.channel.send(embed=emb_mes)

    def get_film_info(self):
        # pull film info from data files
        with open(self.save_embdict_location) as f:
            film_info = json.load(f)
        with open(self.save_magnet_location) as f:
            magnet = json.load(f)

        # return list of embed objects
        return [discord.Embed.from_dict(film_info), discord.Embed.from_dict(magnet)]
