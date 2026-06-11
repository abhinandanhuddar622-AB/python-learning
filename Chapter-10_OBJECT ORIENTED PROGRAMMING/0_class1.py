class Employee:
    company="TaTa"
    E_name="Abhi"

    def salary(self):   #self is important here BCS self is a way to reference the object of the class which is being created
        return 40000
    
    def age(self):
        return 22
    
E1=Employee()        # An Object of class Employee is created  here
print(E1.salary())   #Employee E's get salary method is called

E2=Employee()
print(E2.company)

E3=Employee()
print(E3.E_name)

E4=Employee()
print(E4.age())