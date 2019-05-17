#!/usr/bin/env python3

import os
from time import sleep

f = os.popen('xbacklight -get').read()
ff = ''
for x in f:
    if x.isdigit() or x == '.':
        ff += x
brig = int(float(ff))
print(' {}'.format(brig))
sleep(0.1)

