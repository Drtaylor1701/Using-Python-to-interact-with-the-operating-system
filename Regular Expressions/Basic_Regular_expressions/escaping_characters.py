#!/usr/bin/env python3
'''
special characters can also be searched by escaping them
'''
import re

#check that a string has a dot in it
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r".com", "mydomain.com"))

#backslashes also define some special string characcters, so it could also be that
#raw strings help you avoid this
#python sometimes uses a backslash for some special characters
print(re.search(r"\w*", "this is an example"))
print(re.search(r"\w*", "and_this_is_another"))