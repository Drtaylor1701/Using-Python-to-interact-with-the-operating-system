import re
#to escape a special character, put a \ before it
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

#backslashes are used to define some special string characters
# \n indicates a new line
# \t is for a tab
#using raw strings helps avoid confusion b/c special characters won't be interpreted when generating the string

#python uses \w for any alphanumeric character, including letters, numbers, and underscores
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

# \d matches digits
# \s matches whitespace characters
# \b matches word boundaries

#regex101.com lets you try out regexes