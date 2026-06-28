# Print the multiplication table of a number (entered by user).
n=int(input("Enter multiplication num: "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
