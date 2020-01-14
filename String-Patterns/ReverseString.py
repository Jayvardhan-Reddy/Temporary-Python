#input: hana
#output: anah

class ReverseString:

    #1st Way: (Using Slice operator)
    s=input("Enter Some String:")
    print(s[::-1])

    #2nd Way: (Reversed)
    s=input("Enter Some String:")
    print(''.join(reversed(s)))

    #3rd Way: (Using String Concat)
    s=input("Enter Some String:")
    i=len(s)-1
    target=''
    while i>=0:
        target=target+s[i]
        i=i-1
    print(target)

    #4th Way: (Using List to store)
    s=input("Enter Some String:")
    i=len(s)-1
    target=[]
    while i>=0:
        target.append(s[i])
        i=i-1
    print(''.join(target))
