#input: asd5g7h
#output: adghs57

class AlphaDigit:
    val = str(input("Enter the alpha num to be sorted"))
    alp = []
    dig = []
    for i in val:
        if i.isalpha():
            alp.append(i)
        else:
            dig.append(i)
    res = ''.join(sorted(alp) + sorted(dig))
    print("sorted value is: ", res)