
#has_teen
def has_teen(a, b, c):
    if (19 >= a >= 13) or (19 >= b >= 13) or (19 >= c >= 13):
        return True
    else:
        return False

print has_teen(5, 13, 25)
print has_teen(5, 12, 19)
print has_teen(5, 2, 6), "\n"


# TODO - write not_string

def not_string(s):
    if s[:3] == "not":
        return s[4:] + " not"
    else:
        return "not " + s[::]

print not_string("not bananas")
print not_string("ayy lmao"), "\n"


# TODO - write icy_hot

# TODO - write closer_to

# TODO - write two_as_one

# TODO - write pig_latinify
