from os.path import join
from os import remove

from discord import HTTPException
from emoji import emojize

import settings


def get_rel_path(rel_path):
    """Returns a path relative to the bot directory"""
    return join(settings.BASE_DIR, rel_path)


def get_emoji(emoji_name, fail_silently=False):
    """Returns an emoji as required to send it in a message
    You can pass the emoji name with or without colons
    If fail_silently is True, it will not raise an exception
    if the emoji is not found, it will return the input instead
    """
    alias = emoji_name if emoji_name[0] == emoji_name[-1] == ":" \
        else f":{emoji_name}:"
    the_emoji = emojize(alias, use_aliases=True)

    if the_emoji == alias and not fail_silently:
        raise ValueError(f"Emoji {alias} not found!")

    return the_emoji


def get_channel(client, value, attribute="name"):
    """A shortcut to get a channel by a certain attribute
    Uses the channel name by default
    If many matching channels are found, returns the first one
    """
    channel = next((c for c in client.get_all_channels()
                    if getattr(c, attribute).lower() == value.lower()), None)
    if not channel:
        raise ValueError("No such channel")
    return channel


def get_user(message):
    """
    :param message:
    :return:user (string)
    """
    try:
        # see https://discordpy.readthedocs.io/en/latest/api.html#member
        user = message.author.name
    except:
        # see https://discordpy.readthedocs.io/en/latest/api.html#user
        user = message.author.nick
    return user


def audience_list(names):
    n = len(names)
    return {
        0: 'No audience member yet',
        1: '{} will be in the audience',
        2: '{} will join {} in the audience',
        3: '{} will join {} and {} like this',
        4: '{} will join {} and {} in the audience'
    }[min(4, n)].format(*names)


async def send_in_channel(client, channel_name, *args):
    """Shortcut method to send a message in a channel with a certain name
    You can pass more positional arguments to send_message
    Uses get_channel, so you should be sure that the bot has access to only
    one channel with such name
    """
    # TODO need to migrate to new discord.py
    await client.send_message(get_channel(client, channel_name), *args)
