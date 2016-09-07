#has_teen
def has_teen(a, b, c):
    if (19 >= a >= 13) or (19 >= b >= 13) or (19 >= c >= 13):
        return True
    else:
        return False

print has_teen(5, 13, 25)
print has_teen(5, 12, 19)
print has_teen(5, 2, 6), "\n"


#write not_string
def not_string(s):
    if s[:3] == "not":
        return s[4:] + " not"
    else:
        return "not " + s[::]

print not_string("not bananas")
print not_string("ayy lmao"), "\n"


# TODO - write icy_hot
def icy_hot(a, b):
    if (a > 100 and b < 0) or (b > 100 and a <0):
        return True

print icy_hot(101, -20) #true
print icy_hot(123, 5) #false
print icy_hot(-39, 104) #true
print icy_hot(5, 104) #false
print icy_hot(104, 104) #false
print icy_hot(-23, -23) #false


# TODO - write closer_to

# TODO - write two_as_one

# TODO - write pig_latinify
