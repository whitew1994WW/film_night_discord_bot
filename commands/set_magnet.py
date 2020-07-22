from settings import MOVIE_NIGHT_ROLE
from commands.base_command import BaseCommand


class SetMagnet(BaseCommand):
    def __init__(self):
        description = "Updates the magnet of the film"
        params = ['new_magnet_link']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        # Remove trackers from magnet
        info = self.set_magnet(params[0].split('&tr')[0])

        msg = f"{MOVIE_NIGHT_ROLE} \n\nLink has been added for {info['name']}:\n " \
            f"```{info['magnet']}```"
        await message.channel.send(msg)

    def set_magnet(self, new_magnet):
        info = self.get_info()
        info['magnet'] = new_magnet
        self.set_info(info)
        return info
