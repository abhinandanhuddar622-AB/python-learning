#Multiple if statement

a=int(input("Enter your age: "))

if (a>0):               #any number of if can be used
    print("DOB is: ",2026-a)
if(a>=18):
    print("you can vote")
elif(a<0):              #any number of elif can be used
    print("invalide age")
else:
    print("you conot vote")