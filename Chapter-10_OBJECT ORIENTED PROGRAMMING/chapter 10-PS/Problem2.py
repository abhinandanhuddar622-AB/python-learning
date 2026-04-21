# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class Calculator:                     #class
    def __init__(self,num):             #constructor
        self.num=num

    def square(self):
        print(f"Square of {self.num} is {self.num*self.num}")   #Finds square of number

    def cube(self):
        print(f"Cube of {self.num} is {self.num*self.num*self.num}")  #Finds cube of number

    def square_root(self):
        print(f"Square root of {self.num} is {self.num**0.5}")     #Finds square root of number
a=Calculator(4)    #creating object
a.square()
a.cube()
a.square_root()