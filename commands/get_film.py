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
        super().__init__(description, params)

    async def handle(self, params, message, client):

        # bot reply
        embedded_messages = self.get_film_info()
        # sends film info and magnet link
        await message.channel.send(embed=embedded_messages)

    def get_film_info(self):
        # pull film info from data files
        with open(self.save_embdict_location) as f:
            film_info = json.load(f)

        # return list of embed objects
        return discord.Embed.from_dict(film_info)
