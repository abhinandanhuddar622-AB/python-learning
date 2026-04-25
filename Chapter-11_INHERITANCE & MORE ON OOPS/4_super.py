class employee:
    def __init__(self):
        print("employee class")               #base class
    a="*"

class programmer(employee):   #derived class 1
    def __init__(self):
        print("programmer class")
        super().__init__()                  #
    b="*"

class manager(programmer):    #derived class 2
    def __init__(self):
        print("manager class")
        super().__init__()
    c="*"

d=employee()
print(d.a)                    #print base class

e=programmer()
print(e.a,e.b)                #print derived class 1 only

f=manager()
print(f.a,f.b,f.c)            #print derived class 1 and derived class 2