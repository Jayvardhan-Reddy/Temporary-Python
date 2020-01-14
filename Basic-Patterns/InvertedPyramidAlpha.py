n = int(input("enter the number of rows: "))
for i in range(n):
    print(' '*i,end='')
    for j in range(n-i):
        print(chr(65+j),end=' ')
    print()