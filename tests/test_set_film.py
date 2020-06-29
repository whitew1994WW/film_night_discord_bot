import unittest
from commands.set_film import SetFilm
import os
import json

class TestSetFilm(unittest.TestCase):
    def setUp(self):
        self.class_obj = SetFilm()
        self.params = ['The Film', '12/05/1994', '1:00 PM GMT', 'dfgsdfgsdfgs']

    def test_store_film(self):
        film_file = self.class_obj.save_dict_location
        if os.path.exists(film_file):
            os.remove(film_file)
        self.class_obj.store_films(self.params)
        if not os.path.exists(film_file):
            raise FileNotFoundError("The film file hasn't been created :(")
        with open(film_file) as f:
            film_deets = json.load(f)

        assert film_deets['film_name'] == 'The Film'


if __name__ == '__main__':
    unittest.main()
