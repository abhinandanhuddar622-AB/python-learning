# Write a program that keeps asking the user to enter a password until they
# enter the correct one.

n="Abhi001"

while True:

    i=input("Enter your correct psw:")
    if n==i:
        print("correct psw")
        break
    else:
        print("Psw in not correct retry")
    
print("End")