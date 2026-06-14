# Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it return that new function
def decorator(fanc):
    def wrapper():
        print("I am execute something")
        fanc()
        print("i am executed somthingg")
    return wrapper()

def say_somthing():
        print("Hello")
    
f=decorator(say_somthing)
        