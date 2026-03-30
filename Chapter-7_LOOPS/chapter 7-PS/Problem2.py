# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
#    with S.
#    l = ["Abhi", "Raju", "virat", "Sachin", "Rahul"]

l=["Abhi", "Raju", "virat", "Sachin", "Rahul"]
for i in l:
    if i.startswith("S"):
        print("Hello",i)