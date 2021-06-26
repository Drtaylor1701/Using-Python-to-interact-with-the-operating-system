import re
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Recieved an email for go_nuts95@mail.com"))

#use \number for capture groups
print(re.sub(r"^([\w.-]*), ([\w.-]*)$", r"\2 \1", "Lovelace, Ada"))

#backreferences also use this
