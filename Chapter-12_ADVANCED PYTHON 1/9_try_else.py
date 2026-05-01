try:
    a=int(input("Enter number: "))
    print(a)

except Exception as e:  
    print(e)

else:        # runs only if the try block executes successfully (no exception occurs)
    print("I am inside else")
    

