def greater(x):
    if x>9:
        return True
    else:
        return False
    
a=[2,45,66,4,36,6]
val=list(filter(greater,a))
print(val)