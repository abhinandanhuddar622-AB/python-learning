# Using walrus operator
# Walrus operator (:=) = assign value while checking condition
# walrus operator ---->  :=   <-----

if (n := len([1, 2, 3, 4, 5, 6])) > 3:         
          #len([1, 2, 3, 4, 5]),Assigns value to n,Condition check(in one line)
    
    print(f"List is too long ({n} elements, expected <= 3)")

# Output: List is too long (5 elements, expected <= 3)
