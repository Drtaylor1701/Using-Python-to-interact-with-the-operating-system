#!/usr/bin/env python3

'''i/o streams connect the OS to Python and vice versa'''

data = input("This will come from STDIN: ")
print("Now we write to STDOUT: " + data)
print("Now we generate an error to STDERR " + data + 1)