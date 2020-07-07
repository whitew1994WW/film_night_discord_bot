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

        msg = "Please click the ticket to sign up to updates for this film"
        bot_message = await message.channel.send(msg)
        await discord.Message.add_reaction(bot_message, u"\U0001F39F")
        await discord.Message.add_reaction(bot_message, u"\U0001F9F2")
