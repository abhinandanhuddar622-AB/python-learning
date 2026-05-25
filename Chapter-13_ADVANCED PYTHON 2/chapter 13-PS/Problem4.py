# 4. Write a program to filter a list of numbers which are divisible by 5.

#method 1
def divisible5(n):
    if(n%5==0):   
        return True
    return False
l=[2,45,65,45,65,55,3345,44,87,789897,456,45445]
D=list(filter(divisible5,l))
# Filters numbers divisible by 5 using divisible5() function
print(D)


#method 2
#using lambda function
l=[2,45,65,45,65,55,3345,44,87,789897,456,45445]

D=list(filter(lambda n:n%5==0,l))      
#Filters only numbers divisible by 5 from the list

print(D)