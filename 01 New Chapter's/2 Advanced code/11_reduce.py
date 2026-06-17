from functools import reduce

number=[1,2,3,4,5,6,7]
'''
[1,2,3,4,5,6,7]
[ 3 ,3,4,5,6,7]
[  6  ,4,5,6,7]
[    10 ,5,6,7]
[      15 ,6,7]
[        21 ,7]
[          28 ]
'''

def sum(a,b):
    
    return a+b

print(reduce(sum,number))