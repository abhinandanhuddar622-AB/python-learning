import random
n=random.randint(1,100)
a=-1     #guess are not in -ve number
guesses=1  
while(a!=n):         
    a=int(input("guess the number:"))
    if (a>n):
        print("guess lower number please")
        guesses+=1
    elif(a<n):
        print("guess higher number please")
        guesses+=1

print(f"you have guessed number {a} correctly in {guesses} attempts")
