# 1). Write a program to print multiplication table of a given number using for loop.

i=int(input("Enter number: "))
for j in range(1,11):
    print(i,"*",j,"=",i*j)   # i is input number and j is index 1 to 10
    
#or print(f"{i}*{j}={i*j}")  # f string is used to insert variables or values directly inside a string.   