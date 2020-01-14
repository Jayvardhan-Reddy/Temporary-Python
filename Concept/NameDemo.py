from src.NameCalc import add

# Usually on Importing a Module all the statements under it get executed, to avoid that we have used __name__ in NameCalc to check
# and execute all statements if and only if NameCalc is run(Standalone)

def fun():
    add()
    print("Fun1")

def fun2():
    print("Fun2")


def main():    # can be any name
    fun()
    fun2()
    print("In NameDemo Class: ", __name__)

main()
