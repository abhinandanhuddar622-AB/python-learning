a = 33   # global variable
def fun():
    global a      # tells Python to use the global variable 'a', not create a local one
    a = 3         # modifies the global variable 'a'
    print(a)      # prints updated global value (3)
fun()
print(a)          # prints the same updated global value (3)





print("IF 'global a' IS NOT USED.....")
a = 33   # global variable
def fun():
    a = 3         # creates a NEW local variable 'a' (does NOT affect global 'a')
    print(a)      # prints 3 (local value)
fun()
print(a)          # prints 33 (global value remains unchanged)