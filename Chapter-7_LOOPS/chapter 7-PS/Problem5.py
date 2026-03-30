# 5). Write a program to find the sum of first n natural numbers using while loop.

n=int(input("Enter number: "))
i=1
sum=0     #sum 0 because initial value of sum is 0
while(i<=n):
    sum=sum+i    #sum is incremented by i
    i+=1
print(sum)