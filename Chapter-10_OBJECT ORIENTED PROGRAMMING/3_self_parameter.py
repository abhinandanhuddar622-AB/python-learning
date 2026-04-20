class employee:                      # employee is a class, class is a blueprint
    salary=10000     
    age=25                           # salary, age, company are class attributes
    company="Google"

    def getinfo(self):               # self refers to the object calling the method     
        print(f"salary is {self.salary}")

    @staticmethod                    #decorator , decorator is a function,here not using self,
      # defines a method that does not use self or class data  
    def greet():
        print("Good Morning...")

Abhi =employee()                     #creating new object

Abhi.greet()
Abhi.getinfo()                       #calling getinfo function
employee.getinfo(Abhi)               #calling getinfo function using employee class

#both getinfo function are same