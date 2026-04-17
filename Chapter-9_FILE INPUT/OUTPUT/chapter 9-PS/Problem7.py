# 7. Write a program to find out the line number where python is present from ques 6.

line=1
with open("log.txt") as f:
    lines=f.readlines()

found = False
lineno=1
for line in lines:
    if "python" in line:
        print("python is present in line number",lineno)
        found = True
    lineno+=1
    
if not found:
    print("python is not present")