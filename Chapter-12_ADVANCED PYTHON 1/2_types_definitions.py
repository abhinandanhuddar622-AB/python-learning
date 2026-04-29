# Variable type hint
age: int = 25
# Function type hints
def greeting(name: str,age:int) -> str:     # -> str:  This function returns a string (its not required)
    return f"Hello, {name}!\nage {age}"
# Usage
print(greeting("Alice",age)) 