#   6). Create an empty fictionary. Allow 4 frienfs to enter their favorite language as
#       value anf use key as their names. Assume that the names are unique.


# method 1
f={}
name=input("Enter name: ")
language=input("Enter language: ")
f.update({name:language})
name=input("Enter name: ")
language=input("Enter language: ")
f.update({name:language})
name=input("Enter name: ")
language=input("Enter language: ")
f.update({name:language})
name=input("Enter name: ")
language=input("Enter language: ")
f.update({name:language})
print(f)




# methof 2
f={}
f["Abhi"]="python"
f["Abhishek"]="java"
f["Abhinanfan"]="c++"
f["Abhinav"]="c"
print(f)