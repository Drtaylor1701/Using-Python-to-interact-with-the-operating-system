#!/usr/bin/env python3
'''combining special characters to match patterns'''

import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))

#make it stricter by defining beginning and end
print(re.search(r"^A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

#validating if something is a valid variable name
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable_1"))
print(re.search(pattern, "2_this_is_a_valid_variable_name"))
