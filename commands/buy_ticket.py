"""
A film ticket adds all users with a ticket to the audience list.
The audience will be used as a list of names to 'mention' in
    movie night reminders, or for any updates to a movie night.
There will be two ways to get a film ticket:
    - Using the ticket reaction on any film info message by the
        movie night bot
    - Using this buy ticket command
"""

from commands.base_command import BaseCommand


class BuyTicket(BaseCommand):
    def __init__(self):
        description = "Adds a user to the audience list"
        params = []
        self.user = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        info = self.get_info()

        if self.user:
            name = self.user.name
            # Cleaning up after a reaction instance of the class
            self.set_user(None)
        else:
            name = message.author.name

        # TODO add mention user to ticket purchase
        if name not in info['audience']:
            info['audience'] += [name]
            self.set_info(info)
            msg = f"You bought a ticket!\n Ticket holders: {', '.join(info['audience'])}"
        else:
            msg = f"You already has a ticket\n Ticket holders: {', '.join(info['audience'])}"

        await message.channel.send(msg)

    def set_user(self, user):
        """This set_user method will only be required commands we also want
        to interact with through reactions. It allows the reaction handler
        to set the correct user for SetMagnet.

        We want the functionality of reacting to a bot message
        to get a ticket or to be sent a magnet link, and so the user of the
        message would be the bot, and we do not want to be adding the bot to
        the ticket/audience list or to send itself messages.
        """
        self.user = user
        print('Temporary user set as ', self.user)
