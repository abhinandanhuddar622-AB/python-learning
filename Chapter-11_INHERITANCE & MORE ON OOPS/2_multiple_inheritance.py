class employee:                   #class
    company="Google"
    salary=10000
    def getinfo(self):
        print(f"salary is {self.salary}")

class coder:
    language="python"
    def getlang(self):
        print(f"language is {self.language}")

class programmer(employee, coder):       #mmultiple inheritance  <-----
    #programmer is child class of employee and coder
    company="Microsoft"                
    def get(self):
        print(f"salary is {self.salary}in {self.language} language")

B=employee()
A=programmer()

A.getinfo()    #calling getinfo function
A.getlang()
A.get()