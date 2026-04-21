# 3. Create a class with a class attribute a; create an object from it and set ‘a’
#    directly using ‘object.a = 0’. Does this change the class attribute?

class Employee:
    a = 10
d=Employee()
print(d.a)        #print the class attribute bcs instance attribute is not present
d.a=0             #set instance attribute
print(d.a)        # print the instance attribute bcs instance attribute is present
print(Employee.a) # print the class attribute