# Input: asdfgjl
# Output: Even a d g l
# Output: Odd sfj

class EvenOddCharPrint:
    s = input("Enter the input String: ")

    #1st Way
    print('Character at Even Index')
    i = 0
    while i < len(s):
        print(s[i])
        i+=2
    print('Character at ODD Index')
    i = 1
    while i < len(s):
        print(s[i])
        i += 2

    #2nd Way Slice (slice[starval:EndVal:IncrementbyCal])

    print('Character at Even Index', s[0::2])
    print('Character at ODD Index', s[1::2])
