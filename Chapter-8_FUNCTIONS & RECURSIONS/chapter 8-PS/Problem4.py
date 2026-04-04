# 4). Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if n==1:
            return 1
    else:
            return sum(n-1)+n         #if n=4 then 1+2+3+4, sum(4-1)+4=sum(3)+4
            

n=int(input("Enter number: "))
print(f"Sum of {n} is: {sum(n)}")