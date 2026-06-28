# Ask the user to enter a day number (1–7) and print the corresponding day of
# the week using match case .

N=int(input("Enter nuber b/w 1-7: "))
match N:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("Tuesday")    
    case 4:
        print("Wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("Saturday")