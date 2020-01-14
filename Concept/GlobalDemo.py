
# Global to make the variable Global
# Globals is used to acess global variable

a = 10
print("start of prog a address:  ", id(a))

def something():

    # global a  # It will take consider the global variable a
    a = 9
    x = globals()['a']  # Globals method will have all global variables in it.
    print("In method of prog x address:  ",id(x))
    print("In something method ", a)
    print("In method of prog a address:  ", id(a))
    globals()['a'] = 15

something()