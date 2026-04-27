# 6. Write __str__() method to print the vector as follows:
#    7i + 8j +10k
#    Assume vector of dimension 3 for this problem.

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
        return f"{self.x}i+{self.y}j+{self.z}k"
a=vector(1,2,3)
b=vector(4,5,6)
c=vector(7,8,9)
print(a+b)             #5i+7j+9k
print(a*b)             #32
print(a+c)             #8i+10j+12k
print(a*c)             #50

