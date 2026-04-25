class employee:
    company="Google"                     #class variable
    @classmethod                  #class method <------
    #class method is used to access class variable, 
    #if not use class method then we can't access class variable(company ="Google")

    def show(cls):                #self refers to the object calling the method     
        print(f"company name is {cls.company}")

    @property                      
    def name(self):                #self refers to the object calling the method     
        return f"{self.fname}{self.lname}"

    @name.setter
    def name(self,value):                #self refers to the object calling the method     
        self.fname=value.split()[0]      #split return list(split(" ") Ab AAbb return ['Ab','AAbb'])
        self.lname=value.split()[1]

A=employee()
A.company="Facebook"   
A.name="Abhi Huddar" 
print(A.fname,A.lname)          
A.show()