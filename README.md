# coop - Controls for Chicken Coop Lights, door, etc.

Ensure the following Environment Variables are added to .bashrc:

COOPEMAIL (mail account from which notifications will be sent)
COOPEMAIL_PASS (password of above account)
COOPEMAILRECEIPT (Recipients of the Report)

On new installation create Cron jobs:

@reboot python3 /home/pi/coop/coop_configure.py

* 16 * * * python3 /home/pi/coop/lights_on.py
* 22 * * * python3 /home/pi/coop/lights_off.py
* 7 * * * python3 /home/pi/coop/door_open.py
* 19 * * * python3 /home/pi/coop/door_closed.py

