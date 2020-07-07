import settings
from commands.base_command import BaseCommand


class GetMagnet(BaseCommand):
    def __init__(self):
        description = "Sends magnet link to a user in a direct message"
        params = []
        self.user = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        info = self.get_info()
        magnet = info['magnet']

        if self.user:
            name = self.user.name
            if self.user.dm_channel:
                dm_channel = self.user.dm_channel
                print(f'dm_channel is available for {name}')
            else:
                dm_channel = await self.user.create_dm()
                print(f'No dm_channel available for {name}, create_dm()')
            print('reaction call', name)
            print('reaction call', dm_channel)
            # Cleaning up after a reaction instance of the class
            self.set_user(None)
        else:
            name = message.author.name
            if message.author.dm_channel:
                dm_channel = message.author.dm_channel
                print(f'dm_channel is available for {name}')
            else:
                dm_channel = await message.author.create_dm()
                print(f'No dm_channel available for {name}, create_dm()')
            print('command call', name)
            print('command call', dm_channel)

        await dm_channel.send(f"```{magnet}```")

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
