"""
A film ticket adds all users with a ticket to the audience list.
The audience will be used as a list of names to 'mention' in
    movie night reminders, or for any updates to a movie night.
There will be two ways to get a film ticket:
    - Using the ticket reaction on any film info message by the
        movie night bot
    - Using this buy ticket command
"""

import io
import json
import os

from utils import get_user
import settings
from commands.base_command import BaseCommand


class BuyTicket(BaseCommand):
    def __init__(self):
        description = "Adds a user to the audience list"
        params = []
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        super().__init__(description, params)

    async def handle(self, params, message, reaction_user, client):
        info = self.get_info()
        user = reaction_user.name


        if user not in info['audience']:
            info['audience'] += [user]
            with io.open(self.save_dict_location, 'w') as f:
                f.write(json.dumps(info))
            msg = f"You bought a ticket!\n Ticket holders: {', '.join(info['audience'])}"
        else:
            msg = f"You already has a ticket\n Ticket holders: {', '.join(info['audience'])}"

        await message.channel.send(msg)

    def get_info(self):
        with open(self.save_dict_location) as f:
            info = json.load(f)
        return info
