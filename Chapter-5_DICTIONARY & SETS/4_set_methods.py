s = {1, 5, 32, 54,5, 5, 5, "Abhi"}

print(s, type(s))

#add()
s.add(566)                  #add value
print(s, type(s))
#remove()
s.remove(1)                 #remove value
print(s, type(s))

#union()
s1 = {1, 5, 32, 54,5, 5, 5}
s2 = {1, 5, 32, 54,5, 5, 5, "Abhi"}
s3 = s1.union(s2)           # return unique value 
print(s3, type(s3))

#intersection()
s1 = {1, 5, 32, 54,5, 5, 5}
s2 = {1, 5, 32, 54,5, 5, 5, "Abhi"}
s3 = s1.intersection(s2)    #s1 & s2 return common value
print(s3, type(s3))

#difference()
s1 = {1, 5, 32, 54,5, 5, 5}
s2 = {1, 5, 32, 54,5, 5, 5, "Abhi"}
s3 = s1.difference(s2)     #s1 - s2 
print(s3, type(s3))

#pop()
s1 = {1, 5, 32, 54,5, 5, 5}
s2 = {1, 5, 32, 54,5, 5, 5, "Abhi"}
s3 = s1.pop()              #remove last key and value, Returns removed element 
print(s3, type(s3))

#clear()
s1 = {1, 5, 32, 54,5, 5, 5}
s2 = {1, 5, 32, 54,5, 5, 5, "Abhi"}
s3 = s1.clear()             #remove all key and value
print(s3, type(s3))

#discard()
s1 = {1, 5, 32, 54,5, 5, 5}
s2 = {1, 5, 32, 54,5, 5, 5, "Abhi"}
s3 = s1.discard(5)        #remove 5 from s1 but discard() does NOT return value
print(s3, type(s3))        #discard() does NOT return value
