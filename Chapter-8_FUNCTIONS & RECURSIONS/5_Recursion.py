# Recursion is a function calling itself.
# it is used to directly use a methematic formula as a function.

''' factorial(n) = n*factorial(n-1) '''

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter number: "))
print(f"Factorial of {n} is {fact(n)}")