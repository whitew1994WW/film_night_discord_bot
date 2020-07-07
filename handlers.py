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
    # WARNING
    # There the key for the "getmagnet" value does not render on PyCharm,
    # but there is actually a magnet emoji there. Be careful editing.
    mapping = {"🎟": "buyticket",  # tickets
               "🧲": "getmagnet"}  # magnet, does PyCharm not render this?

    if  reaction_user != bot_client.user and reaction.message.author == bot_client.user:
        cmd_obj = COMMAND_HANDLERS[mapping[str(reaction.emoji)]]
        # sending this message means BuyTicket.handle reads the bot name, as
        #  the bot was the author of the message people are reaction to
        cmd_obj.set_user(reaction_user)
        await cmd_obj.handle([], reaction.message, bot_client)

    # else:
    #     await reaction.message.channel.send(reaction.emoji)
