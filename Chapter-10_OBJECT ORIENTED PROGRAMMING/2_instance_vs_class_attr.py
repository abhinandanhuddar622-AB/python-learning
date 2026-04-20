class employee:       # employee is a class
    sallary=10000     
    age=25            # salary, age, company are class attributes
    company="Google"

Abhi =employee()
Abhi.name="Abhi"      # name is an instance attribute
#instance attribute is unique to each object
print(Abhi.name,Abhi.sallary,Abhi.age,Abhi.company)

Raju=employee()       #Create a new employee object and store it in Abhi
Raju.name="Raju"
Raju.age=28
Raju.sallary=45000
print(Raju.name,Raju.sallary,Raju.age,Raju.company)

# Abhi uses class attributes for salary and age
# Raju overrides salary and age with instance attributes

# Both Abhi and Raju are instances (objects) of employee class
# company remains a class attribute shared by both

