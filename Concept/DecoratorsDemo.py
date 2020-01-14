def div(a,b):
    print (a/b)

def smart_div(func):

    def inner(a,b): # name can be anything but number of parameters should be same
        if a < b:
            a,b = b,a
        return  func(a,b)
    return inner

div = smart_div(div)

div(2,4)

#Imagine if the division code is not with you, i.e, it is part of someother file that we are importing
#We do not have access to this function or the method and we want to swap two values without touching the function
#We can add extra features to the function using Decorators