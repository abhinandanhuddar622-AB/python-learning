class employee:                      # employee is a class, class is a blueprint
    salary=10000     
    age=25                           # salary, age, company are class attributes
    company="Google" 

    def __init__(self,name,salary,age):          # __init__ is a constructor
        # constructor method (called when object is created)

        self.name="Abhi"
        self.salary=salary
        self.age=age
        print("printing __init__ constructor")

abhi =employee("Abhi",1200000,30)         # creating object and passing values to constructor
# accessing instance attributes
print(abhi.name,abhi.salary,abhi.age)