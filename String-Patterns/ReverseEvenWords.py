#Input: Howdy doody
#Output: Howdy ydood

class ReverseEvenWords:
    inp = input("Enter the text")
    s = inp.split()
    arr = []
    i = 0
    while i < len(s):
        if i%2==0:
            arr.append(s[i])
        else:
            arr.append(s[i][::-1])
        i+=1
    print(' '.join(arr))


