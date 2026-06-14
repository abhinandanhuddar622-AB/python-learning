class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @property          #Converts a method into a property
    # Allows access without parentheses ()

    def first_name(self):
        l=self.name.split(" ")     #Splits the name into a list.
        return l[0]
    
    @first_name.setter
    def first_name(self,first):
        l=self.name.split(" ")
        new_name=f"{first} {l[1]}"
        self.name= new_name

e=Employee("Abhi Huddar",40000)
# print(e.first_name())
# e.first_name("Abhinandan")
# print(e.name)

print(e.first_name)
e.first_name="Abhinandan"
print(e.name)
        