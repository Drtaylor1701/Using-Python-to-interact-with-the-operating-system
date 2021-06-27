import csv
f = open("csv_file.txt")
#this creates an instance of the CSV Reader Class
csv_f = csv.reader(f)

#you can now iterate through its contents and access information that is parsed
for row in csv_f:
    #unpack the values so we can use variables to refer to them
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

#close the file when you're done
f.close()