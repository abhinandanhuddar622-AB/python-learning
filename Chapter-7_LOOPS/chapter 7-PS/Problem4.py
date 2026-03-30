# 4). Write a program to find whether a given number is prime or not.

n=int(input("Enter number: "))
for i in range(2,n):           #why range 2 and n because Every number is divisible by 1 
                               #and every number is divisible by its self(n not included))
    
    if(n%i==0):                # n is divisible by i
        print("Number is not prime")
        break
else:
    print("Number is prime")