# 10). Write a program to print multiplication table of n using for loops in reversed
#     order.

n=int(input("Enter number: "))
for i in range(1,11):          #11 because we want to include 10
        print(n,"*",(11-i),"=",n*(11-i))   #n is input number and i is index 1 to 10

        # or print(f"{n}*{11-i}={n*(11-i)}")
        