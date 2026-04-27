# 5. Write a class vector representing a vector of n dimensions. Overload the + and *
#    operator which calculates the sum and the dot(.) product of them.

class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        result=vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return result
    def __mul__(self, other):
        reesult= self.x*other.x+self.y*other.y+self.z*other.z
        return reesult
    def __str__(self):
        return f"vector({self.x},{self.y},{self.z})"
a=vector(1,2,3)
b=vector(4,5,6)
c=vector(7,8,9)
print(a+b)
print(a*b)
print(a+c)
print(a*c)

