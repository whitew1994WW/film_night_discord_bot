import sys

import settings
import discord
import handlers
import shlex
from utils import get_emoji

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from events.base_event import BaseEvent
from events import *
from multiprocessing import Process

# Set to remember if the bot is already running, since on_ready may be called
# more than once on reconnects
this = sys.modules[__name__]
this.running = False

# Scheduler that will be used to manage events
sched = AsyncIOScheduler()


def main(testing=False):
    print("Starting up...")
    client = discord.Client()

    @client.event
    async def on_ready():
        """on_ready may be called multiple times in the event of a reconnect,
        hence the running flag
        """
        if this.running:
            return

        this.running = True

        if settings.NOW_PLAYING:
            print("Setting NP game", flush=True)
            await client.change_presence(
                activity=discord.Game(name=settings.NOW_PLAYING)
            )
        print("Logged in!", flush=True)

        # Enter any messages for the bot to send on its login
        # Really useful for testing
        if testing:
            import datetime
            # TODO use last channel bot messaged in instead,
            #  or have global movie night channel
            #  These are hardcoded for chanel id #
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            await client.get_channel(727105225722429440).send(f'Logged in at {timestamp}!')

        print("Loading events...", flush=True)
        n_ev = 0
        for ev in BaseEvent.__subclasses__():
            event = ev()
            sched.add_job(event.run, 'interval', (client,),
                          minutes=event.interval_minutes)
            n_ev += 1
        sched.start()
        print(f"{n_ev} events loaded", flush=True)

    async def common_handle_message(message):
        """The message handler for both new message and edits"""
        # TODO move this to handlers.py
        text = message.content
        if (text.startswith(settings.COMMAND_PREFIX)
                and text != settings.COMMAND_PREFIX):
            cmd_split = shlex.split(text[len(settings.COMMAND_PREFIX):])
            print('cmd_split', cmd_split)
            try:
                await handlers.handle_command(cmd_split[0].lower(),
                                              cmd_split[1:], message, client)
            except:
                print("Error while handling message", flush=True)
                raise

    async def common_reaction_handler(reaction, user):
        """Action upon reactions this bot's film messages"""
        # TODO move this to handlers.py
        print(reaction.emoji)
        await handlers.handle_reaction(reaction, user, client)

    @client.event
    async def on_message(message):
        await common_handle_message(message)

    @client.event
    async def on_message_edit(before, after):
        """Edited messages will be re-sent to the bot"""
        await common_handle_message(after)

    @client.event
    async def on_reaction_add(reaction, user):
        """Assumes the client has filled cached messages"""
        await common_reaction_handler(reaction, user)

    client.run(settings.BOT_TOKEN)


if __name__ == "__main__":
    main(testing=False)
