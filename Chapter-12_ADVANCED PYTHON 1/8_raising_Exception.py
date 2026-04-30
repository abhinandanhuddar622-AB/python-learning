a=int (input("Enter first number: "))
b=int(input("Enter second number: "))

if(b==0):
    raise ZeroDivisionError("invalid number entered")
else:
    print(f"division of a and b is: {a/b} ")