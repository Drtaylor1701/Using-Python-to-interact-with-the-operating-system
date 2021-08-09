#!/usr/bin/env python3
import shutil
import psutil

"""example stuff"""
# du = shutil.disk_usage("/")
# print(du)

# print(du.free/du.total)

# print(psutil.cpu_percent(0.5))

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free /du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("error!")
else:
    print("Everything is OK!")