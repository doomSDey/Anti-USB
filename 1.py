import pyudev
import os

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    if device.action == 'add':
        print('{} connected'.format(device))
        # do something
        os.system("passwd -e Student")
        os.system("gnome-screensaver-command -l")
