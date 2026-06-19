# 7. Write a program to find out the line number where python is present from ques 6.

line=1
with open("log.txt") as f:
    lines=f.readlines()            #read the lines

found = False                      #check if python is present
lineno=1                           #set line number
for line in lines:                 
    if "python" in line:           # if python is present
        print("python is present in line number",lineno)
        found = True               #set found to true
    lineno+=1                      #increment line number
    
if not found:                      # if python is not present 
    print("python is not present")