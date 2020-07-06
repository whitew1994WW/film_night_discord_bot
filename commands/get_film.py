from commands.base_command import BaseCommand
import settings
import os
import json
import discord



class GetFilm(BaseCommand):

    def __init__(self):
        description = "Returns the current film details"
        params = []
        self.save_embdict_location = os.path.join(settings.BASE_DIR, 'data', 'embed_file.json')
        super().__init__(description, params)

    async def handle(self, params, message, client):

        # bot reply
        embedded_messages = discord.Embed.from_dict(self.get_embed())
        # sends film info and magnet link
        await message.channel.send(embed=embedded_messages)
