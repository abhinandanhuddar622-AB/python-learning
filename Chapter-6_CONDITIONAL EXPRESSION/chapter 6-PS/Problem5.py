# 5). Write a program which finds out whether a given name is present in a list or not.

# using in keyword in list 
l = ["Abhi", "Raju", "Ram", "Abhinandan"]     #list

name = input("Enter your name: ")

if(name in l):        #check name in list if name are capital that also check, input name same as list
    print("Your name is in the list")
else:
    print("Your name is not in the list")