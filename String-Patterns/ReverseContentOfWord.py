# Input: use your brain
# Output: esu ruoy niarb

class ReverseContentOfWord:
    inp = input("enter the string of words")
    splitVal = inp.split()
    revContent = []
    for i in splitVal:
        revContent.append(i[::-1])
    print("final result", ' '.join(revContent))
