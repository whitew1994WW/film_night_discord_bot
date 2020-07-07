from commands.base_command import BaseCommand
import discord


class GetFilm(BaseCommand):

    def __init__(self):
        description = "Returns the current film details"
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):
        info = self.get_info()
        channel = message.channel
        msg = "<Placeholder for Bill's embeds> \n Please click the ticket to sign up to updates for this film"
        bot_message = await channel.send(msg)
        await discord.Message.add_reaction(bot_message, u"\U0001F39F")
        await discord.Message.add_reaction(bot_message, u"\U0001F9F2")
