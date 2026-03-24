# 2). Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

a=int(input("Enter marks: "))
b=int(input("Enter marks: "))
c=int(input("Enter marks: "))

#Check for total percentage
total_percentage=(a+b+c)/3   #total percentage
if (total_percentage>=40):   #check total percentage is greater than 40
    if(a>=33 and b>=33 and c>=33):   # and also check each subject is greater than 33
        print("You have passed",total_percentage)
    else:
        print("You have failed",total_percentage)
else:
    print("You have failed",total_percentage)