
a = 5
b = 10

try:
    print("resource open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as z:
    print("Divide by Zero error: ", z)

except ValueError as v:
    print("Invalid input", v)

finally:
    print("closed finally block")