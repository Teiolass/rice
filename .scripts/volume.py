from time import sleep
import os


cmd = 'amixer sget Master | grep \'Right:\' | awk -F\'[][]\' \'{ print $2 }\''
vol = os.popen(cmd).read()
print(' ' + vol)
sleep(0.1)

