# 1. Create a class “Programmer” for storing information of few programmers
#   working at Microsoft.

class Programmer:
    def __init__(self,name,salary,experience,company):
        self.name=name
        self.salary=salary
        self.experience=experience
        self.company=company

Abhi=Programmer("Abhi",200000,2,"Microsoft")
print(Abhi.name,Abhi.salary,Abhi.experience,Abhi.company)

Raju=Programmer("Raju",300000,3,"Microsoft")
print(Raju.name,Raju.salary,Raju.experience,Raju.company)

Sachin=Programmer("Sachin",300000,4,"Microsoft")
print(Sachin.name,Sachin.salary,Sachin.experience,Sachin.company)

Rahul=Programmer("Rahul",300000,5,"Microsoft")
print(Rahul.name,Rahul.salary,Rahul.experience,Rahul.company)

Ankit=Programmer("Ankit",200000,6,"Microsoft")
print(Ankit.name,Ankit.salary,Ankit.experience,Ankit.company)