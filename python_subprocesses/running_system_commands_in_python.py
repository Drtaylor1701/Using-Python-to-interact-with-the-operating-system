#!/usr/bin/env python3

'''
using Python to interact w/ the OS can happen in a lot of ways

you can also run a program from a Python script
'''

#import the subprocess module
from re import sub
import subprocess

#use subprocess to call date command
print(subprocess.run(['date']))

'''to run the command, a secondary environment is created for the child process, which blocks the parent process

after the parent completes its work, the child process exits and returns control to the parent.
'''

#calling the sleep command
subprocess.run(['sleep', '2'])
#while it is running, the terminal is blocked and cannot be used

#elements following program name are command-line arguments

#try something with an exit status other than 0
result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result)
'''run is great when you don't want to do anything with the output'''
