import subprocess

NOT_FOUND = -1

# set TRUE if you're going to call this from the terminal and want feedback
TERMINAL_FEEDBACK = True

# replace PASSWORD HERE with your password
PASSWORD = "PASSWORD HERE"

# command constants
COMMAND_ON = "1"
COMMAND_OFF = "0"
COMMAND_CURRENT_STATUS = "pmset -g |grep lowpowermode"  # get current low power mode setting
COMMAND_SET_STATUS = f"echo {PASSWORD} | sudo -S pmset -a lowpowermode " # set low power mode to 1 or 0 (actual val gets appended later)

# get current status
bashOut = str(subprocess.Popen(COMMAND_CURRENT_STATUS,
                                 stdout=subprocess.PIPE,
                                 shell=True).communicate())
isLowPower = (bashOut.find(COMMAND_ON) != NOT_FOUND)

# toggle passed on current
COMMAND_SET_STATUS += (COMMAND_OFF if (isLowPower) else COMMAND_ON)

# update terminal response if required
if (TERMINAL_FEEDBACK):
    newStatus = ("OFF" if (isLowPower) else "ON")
    print(f"Low Power Mode: {newStatus}")

# run toggle command
subprocess.run([COMMAND_SET_STATUS], shell=True)
