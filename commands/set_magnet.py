import settings
from commands.base_command import BaseCommand


class SetMagnet(BaseCommand):
    def __init__(self):
        description = "Updates the magnet of the film"
        params = ['new_magnet_link']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        info = self.set_magnet(params[0])
        msg = "{role} \n\nLink has been added for {name}:\n " \
              "```{magnet}```".format(role=settings.MOVIE_NIGHT_ROLE, **info)
        await message.channel.send(msg)

    def set_magnet(self, new_magnet):
        info = self.get_info()
        info['magnet'] = new_magnet
        self.set_info(info)
        return info
