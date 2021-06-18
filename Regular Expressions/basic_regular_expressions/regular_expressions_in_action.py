import re

print(re.search(r"A*a", "Argentina"))
print(re.search(r"A*a", "Azerbajan"))
#beginning of line and end of line characters make it match the whole string
print(re.search(r"^A*a$", "Azerbajan"))
print(re.search(r"^A*a$", "Australia"))

#check for valid variable names
#any number of letters, numbers, underscores, but can't start with a number
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable name"))
print(re.search(pattern, "myvariable1"))
print(re.search(pattern, "2myvariable1"))