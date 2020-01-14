```
Actual Arguments are of 4 types
    - Position
    - Keyword
    - Default
    - Variable Length
```


def add(a,b):   # Formal Argument
    c = a +b
    return c

add(12, 34) # Actual Argument

# Position

def person(name, age):
    print(name)
    print(age)

person("Ckanrk", 50)    # position

# Keyword
# Used when we are not aware of the position of arguments in the method.

person(age=30, name="kpask")

# Default
# A default value for method argument is present and is overriden when passed by the calling method

def facebookRegistration(name, age=18):
    print(name)
    print(age)


facebookRegistration("Ckanrk")  # Default 18 age is considered
facebookRegistration("Ckanrk", 50)  # Default 18 age is overriden to 50

# Variable Length

def sum(a,*b):
    c = a
    for i in b:
        c = c + i
    print(c)

sum(5,9,6,5)

# Variable Length Arguments

def people(name, **data):
    print(name)
    print(data)

people('jay', age= 56, city='berlin', mob=3455 )