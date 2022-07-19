#!/usr/bin/env python3
import re
'''
how to match characters several times
'''

#repeated matches: .* matches any character as many times as possible - even 0

print(re.search(r'Py.*n', "Pygmalion"))
print(re.search(r'Py.*n', "Python Programming")) #matches as many characters as possible
print(re.search(r'Py[a-z]*n', "Python Programming"))
print(re.search(r'Py[a-z]*n', "Pyn"))
# + matches one or more characters
print(re.search(r'o+l+', "goldfish"))
print(re.search(r'o+l+', "woolly"))
print(re.search(r'o+l+', "boil"))
# ? matches 0 or 1 occurrence of a character
print(re.search(r'p?each', "to each their own"))
print(re.search(r'p?each', "peach"))