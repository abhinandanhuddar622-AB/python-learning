# Take a user input string and check if it is a palindrome (same forwards and
# backwards).

str=input("Enter any num or char: ")
if(str==str[: :-1]):
    print("it is a palindrome")
else:
    print("it is not a palindrome")