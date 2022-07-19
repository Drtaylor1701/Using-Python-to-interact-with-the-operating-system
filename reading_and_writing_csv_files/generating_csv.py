#!/usr/bin/env/python3
import csv

#writer function to write to file
hosts = [['workstation.local', '192.168.25.46',],['webserver.cloud','10.2.5.6']]

#open the file in write mode
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    #writer is now an instance of the csv.writer class
    #two functions we can use are writerow and writerows
    writer.writerows(hosts)
    #data has been written
