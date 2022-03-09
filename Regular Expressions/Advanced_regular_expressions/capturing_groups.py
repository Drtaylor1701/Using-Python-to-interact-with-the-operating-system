import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)

print(result.groups())

print(result[0])
print(result[1])
print(result[2])

print("{} {}".format(result[2], result[1]))

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))

print(rearrange_name("Hopper, Grace M."))

def rearrange_name_revised(name):
  result = re.search(r"^(\w*), (\w*\s\w\.|\w)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name_revised("Kennedy, John F.")
print(name)
