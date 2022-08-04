# dark mode
import os

# this is super simple and a little hacky, makes use of the fact that the apple
# script command to turn *on* dark mode will turn it *off* if already on
# (and obviously turn *on* if already *off*)

COMMAND_TOGGLE_DRK_MD = "osascript -e 'tell app \"System Events\" to tell appearance preferences to set dark mode to not dark mode'"
os.system(COMMAND_TOGGLE_DRK_MD)
