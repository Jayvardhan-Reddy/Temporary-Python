# Input: a4b3c4
# Output: aaaabbbcccc

class RepeatCharOnDigits:
    inp = 'a4b3c4'
    out = ''
    alp = []
    dig = []
    for ch in inp:
        if ch.isalpha():
            x = ch
        else:
            out = out + x*int(ch)
    print(out)

    dc = '4a3b4u'

