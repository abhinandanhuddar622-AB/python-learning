# 1. Create a class (2-D vector) and use it to create another class representing a 3-D
#    vector.
class ToDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"{self.i}i + {self.j}j")
class ThreeDVector(ToDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

# i=int(input("Enter i: "))
# j=int(input("Enter j: "))
# k=int(input("Enter k: "))
# v1=ToDVector(i,j)
# v2=ThreeDVector(i,j,k)            # <------Taking user input for vector values (i, j, k)

v1=ToDVector(7,8)
v2=ThreeDVector(7,8,10)
v1.show()
v2.show()