import unittest
from commands.set_film import SetFilm
from commands.get_film import GetFilm
import os
import json

class TestGetFilm(unittest.TestCase):
    def setUp(self):
        self.set_film_class_obj = SetFilm()
        self.get_film_class_obj = GetFilm()
        self.params = ['The Film', '12/05/1994', '1:00 PM GMT', 'dfgsdfgsdfgs']
        self.set_film_class_obj.store_films(self.params)


    def test_get_film_deets(self):
        film_deets = self.get_film_class_obj.get_film_deets()
        assert film_deets['film_name'] == 'The Film'


if __name__ == '__main__':
    unittest.main()
