# 6). Write a python function which converts inches to cms.

def inches_to_cms(inches):
    cms = inches * 2.54
    return cms

inches = float(input("Enter the length in inches: "))
cms = inches_to_cms(inches)
print(f"{inches} inches is equal to {cms} cms.")


# OR

def inches_to_cms(inches):
    return inches * 2.54

n=int(input("Enter the length in inches: "))
print(f"{n} inches is equal to {inches_to_cms(n)} cms.")