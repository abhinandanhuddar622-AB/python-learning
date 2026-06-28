# Write a program using match case that simulates a simple calculator.
#   Ask the user for two numbers and an operation (+, -, *, /).
#   Perform the operation using match case .

Num1=int(input("Enter num1: "))
Num2=int(input("Enter num2: "))

operation=input("Enter operations: ")

match operation:
    case "+":
        print(Num1+Num2)
    case "-":
        print(Num1-Num2)
    case "%":
        print(Num1/Num2)
    case "*":
        print(Num1*Num2)
    case _:
        print("Invalid input")
