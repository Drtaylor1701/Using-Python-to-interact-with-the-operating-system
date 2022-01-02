#!/usr/bin/env python3
import re
import csv

LOGTYPE = r'(ERROR|INFO)'
USERNAME = r'\(([\w.]*)\)$'
ERRORTEXT = r'ERROR ([\D]*) \('
error_dict = {}
user_dict = {}

def read_ticket_type(line):
    '''reads log file and detects ticket type'''
    ticket_type = re.search(LOGTYPE, line)
    ticket_type = ticket_type[1]
    return ticket_type

def read_user_name(line):
    '''reads log file and detects user name'''
    user_name = re.search(USERNAME, line)
    user_name = user_name[1]
    return user_name

def read_error_text(line):
    '''reads error text from error line'''
    error_text = re.search(ERRORTEXT, line)
    error_text = error_text[1]
    #print(error_text)
    return error_text

def add_dict_entry(key_entry, dict_name):
    if key_entry in dict_name:
        dict_name[key_entry] += 1
    else:
        dict_name[key_entry] = 1
    print(dict_name)
    return dict_name

def sort_dict_by_value(dict_name):
    sorted_dict = {}
    for entry in sorted(dict_name, key=dict_name.get, reverse=True):
        sorted_dict[entry] = dict_name[entry]
    #print(sorted_dict)
    return sorted_dict

def sorted_dict_by_key(dict_name):
    dict_to_sort = dict_name.items()
    sorted_dict = sorted(dict_to_sort)
    #print(sorted_dict)
    return sorted_dict

def convert_dict_to_csv(input_dict, csvname, col_list):
    try:
        with open(csvname, 'x', encoding="utf-8") as f:
            fieldnames = col_list
            dictwriter = csv.DictWriter(f, fieldnames=col_list)
            writer = csv.DictWriter(f, fieldnames)
            dictwriter.writerow(fieldnames)
            for entry in input_dict:
                writer.writerow(entry)
    except IOError:
        return "Write error"

with open('Final Project/syslog.log', 'r', encoding="utf-8") as logfile:

    for log in logfile:
        #print(read_ticket_type(log))
        #print(read_user_name(log))
        if read_ticket_type(log) == 'ERROR':
            key_entry = read_error_text(log)
            #print(key_entry)
            add_dict_entry(key_entry, error_dict)
            #print(error_dict)
            sorted_error_dict = sort_dict_by_value(error_dict)
            convert_dict_to_csv(sorted_error_dict, "errors.csv", ['Error Type', 'Occurrences'])
        user_name = read_user_name(log)
        add_dict_entry(user_name, user_dict)
        sorted_dict_by_key(user_dict)
