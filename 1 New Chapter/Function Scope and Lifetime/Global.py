def sum(a,b):
    print("Hey I am summing")
    c=a+b
    global z   # its modify global z
    z=1        # this will refer to global z and not create a local varible

    return c
z=3
print(sum(3,6))

print(z)


# can you modify the global varible inside a function ans:YES (use Global)