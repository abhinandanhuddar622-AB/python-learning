f=open("file.txt","r")
data=f.read()
print(data)
f.close()

print("\n")                         #new line
print("new text file below->")

f=open("read_file.txt","r")       #r means read mode and open the file
data=f.read()
print(data)
f.close()                         #close the file
