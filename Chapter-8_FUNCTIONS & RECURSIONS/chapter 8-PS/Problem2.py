# 2). Write a python program using function to convert Celsius to Fahrenheit.

def f_to_c(f):
    c = 5*(f - 32)/9     # formula
    return c

f = float(input("Enter temperature in Fahrenheit: "))
c = f_to_c(f)          # calling function
print(f"{f} degrees Fahrenheit is equal to {round(c,2)} degrees Celsius.")          # round to 2 decimal