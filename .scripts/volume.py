import alsaaudio as alsa
from time import sleep

m = alsa.Mixer()
vol = m.getvolume()

print(' ' + str(vol[0]) + '%')
sleep(0.1)

