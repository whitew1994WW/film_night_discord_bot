import os
from secrets import token

COMMAND_PREFIX = "!frodo"

# Which role to mention in comments.
# Hard coded for testing, with the role ID which can
# be retrieved by typing in discord: \@RequiredRole
MOVIE_NIGHT_ROLE = "<@&727544315731116083>" # nerd herd
# AUDIENCE = "<@&552462297487114241>"  # the group

BOT_TOKEN = token

NOW_PLAYING = "Artifact with Samwise"

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
