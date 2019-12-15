#!/usr/bin/env python3

import os

f = os.popen('acpi -t').read().split(' ')[3]
f = u'\uf2c7 ' + f[:-2] + u'\u00b0C'
print(f)

