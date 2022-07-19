#!/usr/bin/env/python3
'''csv module to work with csv files'''
import csv
with open("/Users/gillian/Documents/Using-Python-to-interact-with-the-operating-system/reading_and_writing_csv_files/csv_file.txt") as f:
    #instance of the csv_reader class
    csv_f = csv.reader(f)
    #we can now iterate through contents and access information that was parsed
    for row in csv_f:
        #row variable holds each row in the CSV as a list
        #unpack the values and use variables to refer to them
        name, phone, role = row
        #for this to work, we need to have the same number of variables on the left as the sequence on the right
        print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
        #we unpack the row so we don't have to use indexes to find each element
        #makes code more readable