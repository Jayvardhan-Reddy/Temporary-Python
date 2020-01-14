#import NameDemo

def add():
    print("in add")

def sub():
    print("in sub")

def main():
    add()
    sub()
    print("In NameCalc Class: ", __name__)

if __name__ == '__main__':
    main()