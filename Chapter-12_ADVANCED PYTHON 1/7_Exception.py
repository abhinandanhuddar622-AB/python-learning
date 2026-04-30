# Using try-except to handle invalid input and prevent program crash
try:                    
    a=int(input("Enter Number: "))
    print(a)

except Exception as e:         #saves the error message in e
    print(e)
    