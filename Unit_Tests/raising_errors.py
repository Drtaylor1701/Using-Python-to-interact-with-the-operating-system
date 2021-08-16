#!/usr/bin/env python3

def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True


#print(validate_user("", -1))
#print(validate_user("cat", 2))
print(validate_user(88, 1))
