# coop - Controls for Chicken Coop Lights, door, etc.

On new installation create Cron jobs:

@reboot python3 /home/pi/coop/coop_configure.py

* 16 * * * python3 /home/pi/coop/lights_on.py
* 22 * * * python3 /home/pi/coop/lights_off.py
* 7 * * * python3 /home/pi/coop/door_open.py
* 19 * * * python3 /home/pi/coop/door_closed.py

