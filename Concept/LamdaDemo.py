
# Filter
from functools import reduce

num = [2,4,5,6,7,8,9]

evenno = list(filter(lambda n: n%2==0, num))

print("Even numbers: ", evenno)

# Map

doubleval = list(map(lambda n: n*2, evenno))

print("Doubled Values: ",doubleval)

# Reduce

sumval = reduce(lambda a,b:a+b, doubleval)

print("Sum values ", sumval)