
# List -> changeable -> many methods

friends=["apple","1008",True,3.14,"banana",33/2,"cherry"]
print(friends[2])
print(friends[2:6])
print(friends[2:6:3]) #select element in list
#2 to 6 and select every 3rd element

friends[2]=False #change value of list element 
print(friends)   #print changed list

print(len(friends)) # check length of list

friends.append("Abhi") #add element in list
print(friends)

friends.append("Abhi") #add element in list

friends.insert(1,"1ST") #add element in list
print(friends)

friends.remove("apple") #remove element in list
print(friends)

friend=["a","b","c"]
friend.pop() #remove last element in list 
print(friend,"pop")

friends.clear() #remove all element in list
print(friends)

del friends #delete list

friends=["apple","1008",True,3.14,"banana",33/2,"cherry"]
print(friends.index("apple")) #check index of element in list

print(friends.count("apple")) #check how many times element in list

friends2=[1,6,4,8,4,0,4,5,3]
friends2.sort() #sort list
print(friends2)

friends3=[1,6,4,8,4,0,4,5,3]
friends3.reverse() #reverse list
print(friends3)

friends.reverse() #reverse list
print(friends)

friends4=friends2.copy() #copy list
print(friends4)
