#!/usr/bin/env python3

'''opens a log file and reads each line, collecting information about each log.'''
import re

error_dict = dict()

with open('Final Project/syslog.log', 'r') as logfile:
    for line in logfile:
        #print(line, end='')
        LOGTYPE = r'(INFO|ERROR)'
        log_type = re.search(LOGTYPE, line)
        log_type = log_type[1]
        if log_type == 'ERROR':
            #print(line)
            error_text_finder = r'(ERROR )([\D|\s]*)\('
            error_text = re.search(error_text_finder, line)
            print(error_text[2])
        elif log_type == 'INFO':
            info_text_finder = r'(INFO )([\D|\s]*)\('
            info_text = re.search(info_text_finder, line)
            print(info_text)
