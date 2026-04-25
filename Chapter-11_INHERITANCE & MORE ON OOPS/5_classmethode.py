class employee:
    company="Google"                     #class variable
    @classmethod                  #class method <------
    #class method is used to access class variable, 
    #if not use class method then we can't access class variable(company ="Google")

    def show(cls):                #self refers to the object calling the method     
        print(f"salary is {cls.company}")

A=employee()
A.company="Facebook"              #instance variable ,display facebook when not use class method
A.show()