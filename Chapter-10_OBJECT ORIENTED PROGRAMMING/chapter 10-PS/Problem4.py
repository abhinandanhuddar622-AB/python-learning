# 4. Add a static method in problem 2, to greet the user with "Good Morning..."

class Calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"Square of {self.num} is {self.num*self.num}")

    def cube(self):
        print(f"Cube of {self.num} is {self.num*self.num*self.num}")

    def square_root(self):
        print(f"Square root of {self.num} is {self.num**0.5}")

    @staticmethod                       #decorator ,static method  <-------            
    def greet():                                                
        print("Good Morning...")

a=Calculator(4)
a.greet()   #calling static method
a.square()
a.cube()
a.square_root()