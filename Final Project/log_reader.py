#!/usr/bin/env python3

with open('Final Project/syslog.log', 'r') as logfile:
    for line in logfile:
        print(line, end='')
