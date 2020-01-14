# Super keyword is used to call parent class constructor i.e, __init__ method
# Super keyword need not be first statement of the Constructor. Java first call is to the constructor

class A:

    def __init__(self):
        print("Inside A init")

    def feature1(self):
        print("Feature 1 of a working")

    def feature2(self):
        print("Feature 2 of a working")

class B:

    def __init__(self):
        print("Inside B init")

    def feature1(self):
        print("Feature 1 of B working")

    def feature2(self):
        print("Feature 2 of B working")

class C(A,B):

    def __init__(self):
    #    super.__init__()
        print("Inside C init")
        super().__init__()

    def feat(self):
        super().feature2()

c = C()
c.feat()
