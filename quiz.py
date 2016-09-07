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


#icy_hot
def icy_hot(a, b):
    if (a > 100 and b < 0) or (b > 100 and a <0):
        return True
    else:
        return False

print icy_hot(101, -20) #true
print icy_hot(123, 5) #false
print icy_hot(-39, 104) #true
print icy_hot(5, 104) #false
print icy_hot(104, 104) #false
print icy_hot(-23, -23), "\n" #false


#closer_to
def closer_to(a, b, c):
    if abs(a-b) < abs(a-c):
        return b
    if abs(a-b) > abs(a-c):
        return c
    if abs(a-b) == abs(a-c):
        return 0
#   (target, guess, guess)
print closer_to(5, 6, 8)
print closer_to(5, 4, 16)
print closer_to(5, -1, 100)
print closer_to(5, 4, 4)











# TODO - write two_as_one

# TODO - write pig_latinify
