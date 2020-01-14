# Two ways Deep copy and Shallow Copy:
from array import array

#from numpy import *

#Aliasing two Arrays

arr = array('i', [1, 2, 3, 5, 4])

arr1 = arr
print(arr)
print(id(arr))
print(arr1)
print(id(arr1))

#Shallow Copy (or) View
# Creates a new Array at different location
#Changes are affected for both even if one of the array is modified.

aar2 = arr.view()
arr[1] = 10
print(arr)
print(id(arr))
print(aar2)
print(id(aar2))

#Deep Copy
# Creates a new Array at different location
#Changes to one Array does not affect the values of other Array

aar3 = arr.copy()
arr[1] = 15
print(arr)
print(id(arr))
print(aar3)
print(id(aar3))

