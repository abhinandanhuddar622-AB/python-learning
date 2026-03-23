# dict.keys()
# dict.values()
# dict.items()

d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys())              # only keys
print(d.values())            # only values
print(d.items())             # keys and values

# dict.get(key)
d = {'a': 1, 'b': 2, 'c': 3}
print(d.get('a'))            #get value of key
print(d.get('d'))

# dict.pop(key)
#pop remove key
d = {'a': 1, 'b': 2, 'c': 3}
print(d.pop('a'))           #pop value of key
print(d,"pop")              
# get -> only take
# pop -> take + remove

# dict.update()
d = {'a': 1, 'b': 2, 'c': 3}
d.update({'d': 4})           #add new key and value
print(d)

# dict.clear()
d = {'a': 1, 'b': 2, 'c': 3}
d.clear()                   #remove all key and value
print(d)

# dict.copy()
d = {'a': 1, 'b': 2, 'c': 3}
d1 = d.copy()                #copy all key and value
print(d1)

