# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
#    operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r,i):
        self.i=i
        self.r=r
    
    def __add__(self,c2):
        return self.r + c2.r,self.i + c2.i
    
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)
    def __str__(self):
        return (f"self.i + self.r")
        
a=complex(1,2)
b=complex(3,4)
print(a+b)
print(a*b)