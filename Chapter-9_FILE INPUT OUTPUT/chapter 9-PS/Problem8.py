# 8. Write a program to make a copy of a text file “this. txt”

with open("this.txt") as f:   #open the file
    data=f.read()

with open("this_copy.txt","w") as f:   #this is a new file
    f.write(data)   #write the data