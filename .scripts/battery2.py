from time import sleep
import os


cmd = 'acpi'
vol = os.popen(cmd).read()
plugged = not 'remaining' in vol
vol = vol.split(',')[1]
val = int(vol[1:4].replace('%', ''))
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
print(plugged + ' ' + str(val) + '%')
