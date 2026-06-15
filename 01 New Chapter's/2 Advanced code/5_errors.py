while True:
    try:
        n=int(input("Enter Number: "))
        n1=int(input("Enter Number: "))
        print(f"division is:{n/n1}")

    except ValueError:
        print("hey type number")

    except ZeroDivisionError:
        print("hey dont divide by 0")

    except Exception as e:
        print("Unknow error occured",e)