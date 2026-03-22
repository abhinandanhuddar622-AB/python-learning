# Tuple → fixed → only 2 methods
# Tuple has only 2 methods: count() and index()
t = (1, 2, 3, 2, 4, 2)

print(t.count(2))

print(t.index(2))

print(t.index(2, 3))

t = ("apple", "banana", "apple", "mango")

print(t.count("apple"))
print(t.index("banana"))

# Useful tuple operations (not methods)
t = (1, 2, 3, 4, 5)
print(sum(t))
print(min(t))
print(max(t))
print(len(t))

# 