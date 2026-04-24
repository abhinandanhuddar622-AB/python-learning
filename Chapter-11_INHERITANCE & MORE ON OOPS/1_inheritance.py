class employee:                   #class
    company="Google"
    salary=10000
    def getinfo(self):
        print(f"salary is {self.salary}")

class programmer(employee):       #inheritance  <-----
    #programmer is child class of employee
    company="Microsoft"
    def get(self):
        print(f"salary is {self.salary}")

B=employee()
A=programmer()
print(A.company,A.salary)
print(B.company,B.salary)