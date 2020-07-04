import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "!frodo"

# Which role to mention in comments.
# Hard coded for testing, with the role ID which can
# be retrieved by typing in discord: \@RequiredRole
AUDIENCE = "<@&727544315731116083>" # nerd herd
# AUDIENCE = "<@&552462297487114241>"  # the group

# The bot token. Keep this secret!
BOT_TOKEN = ""

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = "Artifact with Samwise"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
