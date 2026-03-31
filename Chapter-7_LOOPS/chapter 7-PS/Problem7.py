# 7). Write a program to print the following star pattern.
#    *
#   ***
#  ***** for n = 3

n=int(input("Enter number: "))
for i in range(1,n+1):            #n+1 because we want to include n
    print(" "*(n-i),end="")       #n-i because we want to print spaces 
                                  # and end="" because we want to print in same line
    print("*"*(2*i-1),end="")     #2*i-1 because we want to print stars, i=1 then 2*1-1=1 and i=2 then 2*2-1=3(odd number)
    print()                       # used to break line after each row 