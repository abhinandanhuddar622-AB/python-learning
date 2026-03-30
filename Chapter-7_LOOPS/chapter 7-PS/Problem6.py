# 6). Write a program to calculate the factorial of a given number using for loop.
#3!=3*2*1=6
#5!=5*4*3*2*1=120

n=int(input("Enter number: "))
fact=1                         #initial value of fact is 1 because 0! = 1 or miltiplication 
for i in range(1,n+1):         #n+1 because we want to include n
    fact=fact*i
print(fact)