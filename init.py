#! /usr/bin/env python

import os
from notebook.auth import passwd

print '> Initialization of the notebook port'
port = input('Enter connection port: ')
print '> Initialization of the notebook password'
sha1 = passwd()
os.system("sed -e 's/sha1:SHA1/{sha1}/g;s/PORT/{port}/g' .config.py > config.py".format(sha1=sha1,port=port))



