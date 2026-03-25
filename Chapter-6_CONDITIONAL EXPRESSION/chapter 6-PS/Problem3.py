# 3. A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", “subscribe this", "click this". Write a program
# to detect these spams.

# using or ,in keyword
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)): #check p1,p2,p3,p4 in message or not
    print("This comment is a spam")

else:                                    #if not in the message print else statement
    print("This comment is not a spam")