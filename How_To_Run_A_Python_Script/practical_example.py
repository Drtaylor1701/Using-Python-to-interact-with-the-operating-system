#!/usr/bin/env python3

import shutil
import psutil

du = shutil.disk_usage("/")
print(du)

psutil.cpu_percent(0.1)
