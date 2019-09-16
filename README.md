# Anti USB
This script detects USB block device connection and logs out user after expiring his password. It aims to reduce copying of program during school/college computer lab classes.

## Dependencies

- Python 3.6
- pyudev library

## How to run?

1. `sudo pip3 install pyudev`
2. `sudo cp -i block-device-detect.py /bin`
3. Open Cron Jobs: `sudo crontab -e`
4. Append to last: `@reboot python3 /bin/block-device-detect.py.py &`
5. `sudo reboot`