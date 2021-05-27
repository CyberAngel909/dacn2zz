

# Program name
APP_NAME = "Demo test"

# Program author
APP_AUTHOR = "dragon"

# Release version: [major].[minor].[build]
APP_VERSION = (0, 1, 0)
APP_VERSION_TAG = "beta"
FULL_APP_VERSION_STRING = "{0}.{1}.{2} {3}".format(APP_VERSION[0],
                                                   APP_VERSION[1],
                                                   APP_VERSION[2],
                                                   APP_VERSION_TAG)

# Title string
APP_TITLE = "{0} {1}".format(APP_NAME, FULL_APP_VERSION_STRING)


# DEVELOPER OPTIONS

# Whether this program is in development mode
# USAGE: Switch to False before building as .exe or similar package to
# enable/disable some end-user features that would otherwise hinder
# development and/or testing of the program.
APP_DEBUG = False

# Whether to enable the experimental renderer threading
ENABLE_THREADING = False
