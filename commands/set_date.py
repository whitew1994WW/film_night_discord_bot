from commands.base_command import BaseCommand
import settings
import os, io
import json
import datetime as dt


class SetDate(BaseCommand):
    def __init__(self):
        description = "Updates the date of the film"
        params = ['new_date']
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        super().__init__(description, params)

    async def handle(self, params, message, client):
        msg = self.set_date(params)
        await message.channel.send(msg)

    def get_film_deets(self):
        with open(self.save_dict_location) as f:
            film_deets = json.load(f)
        return film_deets

    def set_date(self, set_date):

        try:
            set_date = dt.datetime.strptime(''.join(set_date), "%d/%m/%y")
        except ValueError:
            return "DD/MM/YY format required"

        new_date = set_date.strftime('%A %d, %b %Y')
        info = self.get_info()
        embed_dic = self.get_embed()

        info['film_date'] = new_date
        try:
            time = info['film_time']
        except KeyError:
            time = '*No time set*'
        embed_dic["fields"][2]["value"] = "{} - {}".format(time, new_date)

        self.set_info(info)
        self.set_embed(embed_dic)

        return 'Film is scheduled for {}'.format(new_date)
