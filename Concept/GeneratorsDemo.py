# Yield is the keyword used for Generator
# Suppose if there are thoussand values and we don't want to load everything into the memory then we can
# use Generators or Yield to fetch one value at a time
# return will terminate function but yeild will not

def topten():

    n = 1

    while n <=10:
        sq = n*n
        yield sq
        n +=1

values = topten()

for i in values:
    print(i)