import re
result = re.search(r"aza", "plaza")
# the r indicates this is a rawstring and python shouldn't try to interpret any special characters
# always use rawstrings for regular expressions in python
print(result)
#result is a match object
result = re.search(r"aza", "bazaar")
print(result)
result = re.search(r"aza", "maze")
print(result)
#none is a special vaule that shows there is no value

print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

#re.IGNORECASE makes it case insensitive
print(re.search(r"p.ng", "Pangea", re.IGNORECASE))