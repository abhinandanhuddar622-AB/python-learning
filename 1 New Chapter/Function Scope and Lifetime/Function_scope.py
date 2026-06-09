# There are 2 types in scope
# 1. Local Scope
# 2. Global Scope

def sum(a,b):
# a and b are local varibles
    c=a+b
    return c

s=4   # s is a global varible  
print(sum(3,6))