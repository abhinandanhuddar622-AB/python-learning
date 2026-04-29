# You can import List, Tuple and Dict types from the typing module like this:
from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types
# Union allows the variable to be either int or str
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid
