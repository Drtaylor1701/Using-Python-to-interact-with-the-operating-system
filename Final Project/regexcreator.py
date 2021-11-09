def createRegex(inputs):
    return "^(" + '|'.join(map(re.escape, inputs)) + )$"

        createRegex("Jun 1 11:46:48 ubuntu.local.ticky: ERROR: Connection to DB failed (username)",
    "May 27 11:45:40 ubuntu.local.ticky: INFO: Created ticket [#1234] (username)")
