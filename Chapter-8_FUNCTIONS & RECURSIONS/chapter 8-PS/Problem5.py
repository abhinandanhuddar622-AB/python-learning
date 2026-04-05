# 5. Write a python function to print first n lines of the following pattern:
#    ***
#    **    - for n = 3
#    *

def pattern(n):
    for i in range(1,n+1):
        for j in range(i,n+1):
            print("*",end=" ")
        print()


n=int(input("Enter number: "))
pattern(n)


# OR (using recursion)

def pattern(n):
    if n==0:
        return
    print("*"*n)      #* is multiplied by n,if n=3 then ***
    pattern(n-1)

n=int(input("Enter number: "))
pattern(n)      