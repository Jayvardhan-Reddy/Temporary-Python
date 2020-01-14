# Method Overloading & Method Overriding
# Python does not have Method overloading unlike other languages eg: Java

# Method Overloading can be achieved by passing default value "None"

class Student:

    def __init__(self):
        print("In Student init")

    if __name__ == '__main__':
        print("In Student main")

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a !=None and b !=None and c !=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

s = Student()
s1 = Student()

print(s.sum(10,20))
print(s1.sum(70,80,20))

# Overriding

class A:

    def show(self):
        print("in A show")

class B(A):

    def show(self):
        print("in B show")

b = B()
b.show()