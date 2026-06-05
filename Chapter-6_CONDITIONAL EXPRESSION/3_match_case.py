a=int(input("Enter number between 1 to 10: "))
match a:
    case 2:
        print("You won the pen")
    case 4:
        print("You won the Book")
    case 6:
        print("You won the bag")
    case 8:
        print("You won the imp Notes")
    case 10:
        print("you won the 5+ study kit")
    case _:
        print("Better luck next time")