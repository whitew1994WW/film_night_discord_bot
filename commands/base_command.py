import settings
import os
import json

class BaseCommand:

    def __init__(self, description, params):
        self.name = type(self).__name__.lower()
        self.params = params
        self.save_dict_location = os.path.join(settings.BASE_DIR, 'data', 'current_film.json')
        self.save_embdict_location = os.path.join(settings.BASE_DIR, 'data', 'embed_file.json')
        desc = f"**{settings.COMMAND_PREFIX} {self.name}**"

        if self.params:
            desc += " " + " ".join(f"*<{p}>*" for p in params)

        desc += f": {description}."
        self.description = desc

    def get_info(self):
        with open(self.save_dict_location) as f:
            return json.load(f)

    def set_info(self, info):
        with open(self.save_dict_location, 'w') as f:
            f.write(json.dumps(info, indent= 1))

    def get_embed(self):
        with open(self.save_embdict_location) as f:
            return json.load(f)

    def set_embed(self, info):
        with open(self.save_embdict_location, 'w') as f:
            f.write(json.dumps(info, indent= 1))
