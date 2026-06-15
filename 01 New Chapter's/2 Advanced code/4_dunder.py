class Dunder():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __str__(self):
        return f"Name of the Employee is {self.name} and salary of employee is {self.salary}"
    
    def __repr__(self):
        return f"Name: {self.name}\nsalary: {self.salary}"
    
    def __len__(self):
        return len(self.name)

d=Dunder("Abhi",40000)
print(d.name,d.salary)
print(str(d))
print(repr(d))
print(len(d))