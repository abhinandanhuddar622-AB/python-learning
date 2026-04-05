# 8). Write a python function to print multiplication table of a given number.

def table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)       #i=1 to 10,n is input number 

n=int(input("Enter number: "))
table(n)