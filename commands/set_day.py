from commands.base_command import BaseCommand
import datetime as dt
import calendar


class SetDay(BaseCommand):
    def __init__(self):
        description = "Updates the scheduled day for the film"
        params = ['day']
        super().__init__(description, params)

    async def handle(self, params, message, client):
        msg = self.set_day(params)
        await message.channel.send(msg)

    def set_day(self, setday):

        setday = ''.join(setday).capitalize()
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

        new_date = datenow + dt.timedelta(days=daydelt)
        new_date = new_date.strftime('%A %d, %b %Y')

        info = self.get_info()
        embed_dic = self.get_embed()

        info['date'] = new_date
        try:
            time = info['time']
        except KeyError:
            time = '*No time set*'
        embed_dic["fields"][2]["value"] = "{} - {}".format(time, new_date)

        self.set_info(info)
        self.set_embed(embed_dic)

        return 'Film is scheduled for {}'.format(new_date)
