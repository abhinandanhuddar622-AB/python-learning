l=[3,56,765,44,23,67]

# index=0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index+=1

#This can be SIMLIFIED using enumerate function

for index, item in enumerate(l):    #gives (index, value) while looping
     print(f"The item number at index {index} is {item}")
