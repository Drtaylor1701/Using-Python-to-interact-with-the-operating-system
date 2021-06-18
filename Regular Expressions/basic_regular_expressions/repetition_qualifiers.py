import re

#.* will match any character repeated as many times as possible including 0
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))

#this is called greedy

#only matches letters
print(re.search(r"Py[a-z]*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Pyn"))

#additional repetition qualifiers
# + matches one or more occurrences of the pattern that comes before it
print(re.search(r"o+l+", "goldfish"))
#shows the shortest possible matching string
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

# ? 0 or 1 occurrence of the character before it
print(re.search(r"p?each", "To each their own."))
print(re.search(r"p?each", "I like peaches."))