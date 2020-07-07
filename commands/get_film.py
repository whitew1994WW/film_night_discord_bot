from commands.base_command import BaseCommand
import discord



class GetFilm(BaseCommand):

    def __init__(self):
        description = "Returns the current film details"
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):
        embedded_messages = discord.Embed.from_dict(self.get_embed())
        await message.channel.send(embed=embedded_messages)
