from commands.base_command import BaseCommand

from commands import *
from utils import get_user
import settings

COMMAND_HANDLERS = {c.__name__.lower(): c()
                    for c in BaseCommand.__subclasses__()}


async def handle_command(command, args, message, bot_client):
    if command not in COMMAND_HANDLERS:
        return

    print(f"{message.author.name}: {settings.COMMAND_PREFIX}{command} "
          + " ".join(args))

    cmd_obj = COMMAND_HANDLERS[command]
    if cmd_obj.params and len(args) < len(cmd_obj.params):
        # TODO add author mention to this message
        # TODO how to handle extra parameters
        await message.channel.send("Insufficient parameters!")
    else:
        await cmd_obj.handle(args, message, bot_client)


async def handle_reaction(reaction, reaction_user, bot_client):
    # Emoji to command
    # TODO use utils.get_emoji here, it supports the proper magnet emoji
    mapping = {"🎟️": "buyticket",
               "🔗": "getmagnet"}  # '\U0001f9f2' is magnet

    if reaction.emoji == "🎟️" and bot_client.user == reaction.message.author:
        cmd_obj = COMMAND_HANDLERS['buyticket']
        # sending this message means BuyTicket.handle reads the bot name, as
        #  the bot was the author of the message people are reaction to
        cmd_obj.set_user(reaction_user)
        await cmd_obj.handle([], reaction.message, bot_client)
    else:
        await reaction.message.channel.send(reaction.emoji)
