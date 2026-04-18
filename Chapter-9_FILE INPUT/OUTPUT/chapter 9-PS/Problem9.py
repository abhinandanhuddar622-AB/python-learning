# 9. Write a program to find out whether a file is identical & matches the content of
#    another file.

with open("file1.txt") as f:  #open the file1
    content1=f.read()

with open("file2.txt") as f:  #open the file2
    content2=f.read()

if content1==content2:        #if content1 is equal to content2
    print("file is identical")
else:
    print("file is not identical")