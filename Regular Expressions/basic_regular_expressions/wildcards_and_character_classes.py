import re

#special character that can match any character .

#character classes are written in [] and list the characters we want to match inside those brackets

print(re.search(r"[Pp]ython", "Python"))

#define a range of characters with a dash
print(re.search(r"[a-z]way", "The end of the highway"))

print(re.search(r"[a-z]way", "What a way to go"))

#you could also say [A-Z] or [0-9]
#combine as many ranges and symbols as you want with [a-zA-Z0-9]
print(re.search(r"[a-zA-Z0-9]", "cloudy"))
print(re.search(r"[a-zA-Z0-9]", "cloud9"))

#to match characters not in a group use a [^]
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

#to match one expression or another, use [|]
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I like dogs."))
print(re.search(r"cat|dog", "I like cats and dogs."))

#to get all possible matches, use the findall function
print(re.findall(r"cat|dog", "I like cats and dogs."))