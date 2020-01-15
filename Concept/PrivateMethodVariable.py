#Private methods & variables

class Hello:
  def __init__(self, name):
    self.a = 10
    self._b = 20
    self.__c = 30
    
  def public_method(self):
    print(self.a)
    print(self._b)
    print(self.__c)
    self.__private_method()
    
  def __private_method(self):
    print('private')
    
hello = Hello('Hey')
print(hello.a)
print(hello._b)
#print(hello.__c) # Cannot use outside the class
hello.public_method()
#hello.__private_method() # Cannot use outside the class
