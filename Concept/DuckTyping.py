# Here "Execute (can be any name)" method is used irrespective of it's implementation.
# Similar to Interface

class PyCharm:

    def execute(self):        # The execute method is implemented
        print("Compiling")
        print("Executing")

class Eclipse:

    def execute(self):        # The execute method is implemented
        print("spell check")
        print("Compiling")
        print("Executing")

class Laptop:           # Similar to Interface

    def code(self, ide):
        ide.execute()   # Here this acts like a Interface method signature. i.e, execute

#ide = PyCharm()
ide = Eclipse()

l1 = Laptop()
l1.code(ide)