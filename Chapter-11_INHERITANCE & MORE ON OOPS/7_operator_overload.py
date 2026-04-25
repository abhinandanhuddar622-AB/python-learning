#operator overloading--> redefining operators using special methods
class number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):            #operator overloading
        #addition
        return self.n+num.n
    def __sub__(self,num):            #subtraction        
        return self.n-num.n
    def __mul__(self,num):            #multiplication
        return self.n*num.n
    def __truediv__(self,num):        #division, returns with float 
        return self.n/num.n
    def __floordiv__(self,num):       #floor division, returns quotient without decimal 
        return self.n//num.n
    def __mod__(self,num):            #mod returns remainder
        return self.n%num.n
    def __str__(self):                #returns string
        return f"{self.n}"
    def __len__(self):                #returns length
        return self.n
    #__len__ returns whatever you define
    
n=number(10)
m=number(3)

print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n//m)
print(n%m)
print(n)
print(m)
print(len(n))