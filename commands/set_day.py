from commands.base_command import BaseCommand
import settings
import os, io
import json
import datetime as dt
import calendar


class SetDay(BaseCommand):
    def __init__(self):
        description = "Updates the scheduled day for the film"
        params = ['day']
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        self.save_embdict_location = os.path.join(settings.BASE_DIR, 'data', 'embed_file.json')
        super().__init__(description, params)

    async def handle(self, params, message, client):

        filmday = self.set_day(params)
        msg = filmday
        await message.channel.send(msg)

    def set_day(self, params):
        info = self.get_info()
        embed_dic = self.get_embed()
        setday = ''.join(params).capitalize()
        datenow = dt.date.today()
        todayint = datenow.weekday()
        try:
            if len(setday) < 6:
                setdayint = list(calendar.day_abbr).index(setday)
            else:
                setdayint = list(calendar.day_name).index(setday)

        except ValueError:
            return "{} is not a day dummy.".format(setday)

        if setdayint > todayint:
            daydelt = setdayint - todayint
        else:
            daydelt = 7 - (todayint - setdayint)

        filmdate = datenow + dt.timedelta(days=daydelt)
        filmdate = filmdate.strftime('%A %d, %b %Y')

        info['film_date'] = filmdate

        try:
            time = info['film_time']
        except KeyError:
            time = '*No time set*'

        embed_dic["fields"][2]["value"] = "{} - {}".format(time, filmdate)

        self.set_info(info)
        self.set_embed(embed_dic)

        return 'Film is scheduled for {}'.format(filmdate)


