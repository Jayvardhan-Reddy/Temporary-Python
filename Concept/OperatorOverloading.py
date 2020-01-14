
class Student:

    def __init__(self, m1 , m2):
        #print("inside Init method")
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        c = Student(m1, m2)
        return c

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)
      #  return self.m1, self.m2

s = Student(20,30)
s1 = Student(40,50)
s2 = s + s1
print(s2)