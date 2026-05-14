from functools import reduce

l=[2,4,6,8]
square= lambda x:x*x

sqList=map(square,l)
print(list(sqList))

# print(list(map(str,sqList)))  
# this would convert elements to string, but won't work here because sqList is already consumed

#----->Filter Example
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven=filter(even,l)
print(list(onlyEven))

# Reduce Function
def sum(a,b):
    return a+b
print(reduce(sum,l))

