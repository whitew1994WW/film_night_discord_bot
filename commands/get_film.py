from commands.base_command import BaseCommand
import settings
import os
import json
import discord



class GetFilm(BaseCommand):

    def __init__(self):
        description = "Returns the current film details"
        params = []
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        self.save_embdict_location = os.path.join(settings.BASE_DIR, 'data', 'embed_file.json')
        self.save_magnet_location = os.path.join(settings.BASE_DIR, 'data', 'magnet.json')
        super().__init__(description, params)

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
