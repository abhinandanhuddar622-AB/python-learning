Name="Abhi"

#slicing
print("N 1",Name[-1])   #-1 is last index
print("N",Name[-1:-3])    #-1 to -3 index not include
print("N L",Name[-3:-1])  #-3 to -1 index include
print(Name[1:3])          #1 to 3 index include
# print(c)

a="0123456789"
b=a[1:5:2]      #1 to 5 index include and 1 index skip and 2 index print
c=a[1:8:3]      #1 to 8 index include and 1 and 2index skip and 3 index print     
print(b)
print(c)