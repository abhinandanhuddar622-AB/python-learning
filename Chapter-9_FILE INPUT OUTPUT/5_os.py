import os

a=os.listdir("problems")  # get all list and files
print(a)

print(os.getcwd())   #get current working directory

print(os.path.exists("problems"))  #if file exist get True

os.remove("name.txt")   #Enter_file_name

# os.rmdir("dir")