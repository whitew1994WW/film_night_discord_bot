from commands.base_command import BaseCommand
import settings
from datetime import datetime


class SetDate(BaseCommand):
    def __init__(self):
        description = "Updates the date of the film"
        params = ['new_date']
        super().__init__(description, params)

    async def handle(self, params, message, client):

        info = self.set_date(params[0])
        msg = "{role} \n\n{name} has been set for {date}" \
              "at {time}.\n ".format(role=settings.MOVIE_NIGHT_ROLE, **info)
        await message.channel.send(msg)

    def set_date(self, new_date):
        info = self.get_info()
        try:
            datetime.strptime(new_date, "%d/%m/%Y")
        except ValueError:
            return "Please provide the date in the format 'DD/MM/YYYY'"

        info['date'] = new_date
        self.set_info(info)
        return info
