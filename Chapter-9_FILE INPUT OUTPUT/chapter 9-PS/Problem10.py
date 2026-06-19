# 10. Write a program to wipe out the content of a file using python.

with open("empty.txt","w") as f:  #open the file in write mode
    f.write("")                   #wipe out the content