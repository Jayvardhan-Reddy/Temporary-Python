# Input: aaaabbbccz
# Output: 4a3b2c1z

s='aaaabbbccz'
output=''
previous=s[0]
i=1
size=len(s)
count=1
while i<size:
    if previous == s[i]:
        count +=1
    else:
        output = output+str(count)+previous
        previous = s[i]
        count = 1
    if i == (size-1):
        output = output + str(count) + previous
    i+=1
print(output)

