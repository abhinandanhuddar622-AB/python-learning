# 1). Write a program using functions to find greatest of three numbers

def greatest(a,b,c):              #function
    if(a>b and a>c):              #condition
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
print("Greater number is: ",greatest(a,b,c))