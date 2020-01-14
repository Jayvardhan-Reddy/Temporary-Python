# Fibonacci Sequence

#1st Way
a, b = 0,1
for i in range(0,10):
    print(a)
    a,b = b, a+b

#2nd Way (Using Generators)

def fib(num):
    a,b = 0,1
    for i in range(0,num):
        yield "{}: {}".format(i+1, a)
        a,b = b, a+b

for item in fib(10):
    print(item)
