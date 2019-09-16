#!/bin/bash/python3

import pyudev
import os
import time

user = 'student'
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('block')

print('Monitor script is running!')

for device in iter(monitor.poll, None):
    if device.action == 'add':
        print('{} connected'.format(device))
        # Expire password
        os.system("passwd -e student")
        # Kill user
        logout_command = "pkill -KILL -u " + user
        os.system(logout_command)
    time.sleep(1)
