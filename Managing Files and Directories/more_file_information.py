import os

#returns file size
os.path.getsize()

#returns the last modified time of file in unix timestamp format
os.path.getmtime()

import datetime
timestamp = os.path.getmtime("spider.txt")
#returns a timestamp in a human-readable format
datetime.datetime.fromtimestamp(timestamp)

#returns absolute path of a file
os.path.abspath()