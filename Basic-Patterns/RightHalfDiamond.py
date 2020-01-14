n = int(input("enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(chr(64+j+1), end=' ')
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print(chr(64+j+1), end=' ')
    print()