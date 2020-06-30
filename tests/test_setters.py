import unittest
from commands.set_film import SetFilm
from commands.set_date import SetDate
from commands.set_magnet import SetMagnet
from commands.set_time import SetTime
import os
import json

class TestSetters(unittest.TestCase):
    def setUp(self):
        self.class_obj = SetFilm()
        self.params = ['The Film', '12/05/1994', '1:00 PM GMT', 'dfgsdfgsdfgs']
        self.class_obj.store_films(self.params)
        self.film_file = self.class_obj.save_dict_location

    def test_set_date(self):
        setter = SetDate()
        setter.set_date('13/05/1994')
        with open(self.film_file) as f:
            film_deets = json.load(f)

        assert film_deets['film_date'] == '13/05/1994'

    def test_set_time(self):
        setter = SetTime()
        setter.set_time('3:00 PM GMT')
        with open(self.film_file) as f:
            film_deets = json.load(f)

        assert film_deets['film_time'] == '3:00 PM GMT'

    def test_set_magnet(self):
        setter = SetMagnet()
        setter.set_magnet('new_magnet')
        with open(self.film_file) as f:
            film_deets = json.load(f)

        assert film_deets['film_magnet'] == 'new_magnet'


if __name__ == '__main__':
    unittest.main()
