def divide(a,b):
    try:
        d=a/b
        print(d)
        return d
    except Exception as e:
        print(e)
        return None
    
    # this finally is always run if try run or not but finally always run
    finally:
        print("This is always run")

a=int(input("Enter Number: "))
b=int(input("Enter Number: "))
dd=divide(a,b)