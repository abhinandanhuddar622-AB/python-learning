# 5. Write a program to find the maximum of the numbers in a list using the reduce
#    function.


from functools import reduce
L=[23,45,456,4,30,55,66,23,899]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,L))
# is used to reduce multiple values into a single value.