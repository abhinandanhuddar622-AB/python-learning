class Employee:
    company="BMW"
    def __init__(self,Name,salary,company):
        self.Name=Name
        self.salary=salary
        self.company=company

E1=Employee("Abhi",40000,"TATA")
print(E1.company)        #will always print instance attribute whenever present
print(Employee.company)  # This will always print the class attribute

#object introspection
print(dir(E1))