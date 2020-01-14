from array import array

arr = array('i', [])
arrSize = int(input("Enter the size: "))

findVal = int(input("Enter the value to find: "))

for i in range(arrSize):
    arrVal = int(input("Enter the number: "))
    arr.append(arrVal)

for k in arr:
    if k == findVal:
        print("found")
        break
    k+=1
else:
    print("not found")
