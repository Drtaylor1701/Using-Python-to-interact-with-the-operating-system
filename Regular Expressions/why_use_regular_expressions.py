import re

log = "some stuff bad_process[12345] some more stuff"

regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result)