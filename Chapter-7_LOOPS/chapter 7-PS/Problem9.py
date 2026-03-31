# 9). Write a program to print the following star pattern.
# ***
# * *    for n = 3
# ***

n=int(input("Enter number: "))
for i in range(1,n+1): 
    if i==1 or i==n:          # only first and last row
        print("*"*n,end="")   #* is multiplied by n,if n=3 then * * * 
    else:                     # middle row (not first and last row)
        print("*",end="")    
        print(" "*(n-2),end="")   #n-2 because we want to print spaces, -2 because if n=3 then *1 spaces*
        print("*",end="")         #print * after spaces
    print()                       # used to break line after each row
   