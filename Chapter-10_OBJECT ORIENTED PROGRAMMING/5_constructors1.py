class Employee:
    def __init__(self,Name,salary,company):
        self.Name=Name
        self.salary=salary
        self.company=company

    def Name1(self):
        return self.Name
        


E1=Employee("Abhi",40000,"TATA")
print(E1.Name1())