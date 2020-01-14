# Input1: hello
# Input2: train
# Output: hterlalion

class MergeTwoStringCharAlternately:
    s1 = input("enter String-1: ")
    s2 = input("enter String-2: ")
    i,j=0,0
    output = ''
    while i<len(s1) or j<len(s2):
        if i<len(s1):
            output=output+s1[i]
            i+=1
        if j<len(s2):
            output = output + s2[j]
            j+= 1
    print("Merged value:= ", output)