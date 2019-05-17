#!/usr/local/bin/python3

import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
percent = percent.split('.')[0]
val = int(percent)
if not plugged:
    # plugged=""
    if val > 90:
        plugged = ''
    elif val > 70:
        plugged = ''
    elif val > 40:
        plugged = ''
    else:
        plugged = ''
else:
    plugged=""
print(plugged + str(val) + '%')
