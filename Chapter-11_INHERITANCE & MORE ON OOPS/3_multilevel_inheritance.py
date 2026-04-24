class employee:               #base class
    a="*"

class programmer(employee):   #derived class 1
    b="*"

class manager(programmer):    #derived class 2
    c="*"

d=employee()
print(d.a)                    #print base class

e=programmer()
print(e.a,e.b)                #print derived class 1 only

f=manager()
print(f.a,f.b,f.c)            #print derived class 1 and derived class 2