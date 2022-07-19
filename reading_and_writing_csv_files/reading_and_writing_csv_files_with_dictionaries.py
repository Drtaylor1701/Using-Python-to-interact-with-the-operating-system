#!/usr/bin/env/python3
import csv
'''if you don't know the fields, you can use a dictionary instead of a list to hold all the data
'''

#DictReader turns each row into a dictionary
with open('/Users/gillian/Documents/Using-Python-to-interact-with-the-operating-system/reading_and_writing_csv_files/software.csv', 'r') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row['name'],row['users']))

#DictWriter can generate a csv
#first we need a list of dictionaries
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT Infrastructure"}, {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, {"name": "Charlie Gray", "username": "grayc", "department": "Development"}]

keys = ["name", "username", "department"]
with open ('/Users/gillian/Documents/Using-Python-to-interact-with-the-operating-system/reading_and_writing_csv_files/by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
