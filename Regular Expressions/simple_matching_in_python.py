import re
result = re.search(r"aza", "plaza")
print(result)

#always use raw strings for regular expressions in Python

#output is the position in the string that matchd and what the actual matching string was:
#<re.Match object; span=(2, 5), match='aza'>

result = re.search(r"aza", "bazaar")
print(result)

#output is <re.Match object; span=(1, 4), match='aza'>

result = re.search(r"aza", "maze")
print(result)
#output is None

print(re.search(r"^x", "xenon"))
#output is <re.Match object; span=(0, 1), match='x'>

print(re.search(r"p.ng", "penguin"))
#outputs <re.Match object; span=(0, 4), match='peng'>

print(re.search(r"p.ng", "clapping"))
#<re.Match object; span=(4, 8), match='ping'>

print(re.search(r"p.ng", "sponge"))
#<re.Match object; span=(1, 5), match='pong'>

#make match case insentitive
print(re.search(r"p.ng", "Pangea", re.IGNORECASE))
#<re.Match object; span=(0, 4), match='Pang'>