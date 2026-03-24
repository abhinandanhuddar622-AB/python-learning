#if elif else ladder
a=int(input("Enter your age: "))
if(a>=18):
    print("You can vote") 

elif(a<0):
    print("Invalid age")

else:
    print("You can't vote")