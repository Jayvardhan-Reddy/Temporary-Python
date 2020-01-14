#input: ding dong
#output: dongding

class ReverseWords:

    #1st Way
    inp = str(input("enter the string"))
    inpSplit = inp.split()
    revWords = []
    for i in inpSplit:
        revWords.append(i)
    print(' '.join(reversed(revWords)))

    #2nd Way
    inp = str(input("enter the string"))
    inpSplit = inp.split()
    fin = inpSplit[::-1]
    finalVal = ''.join(fin)
    print(finalVal)

    #3rd Way (changes to be done)
    wordslen = len(inpSplit)-1
    revWords = []
    while wordslen > 0:
        revWords.append(wordslen)
        wordslen-=1
    print(revWords)


