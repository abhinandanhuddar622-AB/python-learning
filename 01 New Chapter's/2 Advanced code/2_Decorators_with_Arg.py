def repeat(n):
    def decorator(fanc):
        def wrapper(a):
            for i in range(n):
                fanc(a)
        return wrapper
    return decorator
@repeat(5)
def say_hello(a):
    print(f"Hello! {a}")


    
say_hello("Abhinandan")