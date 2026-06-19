# 2. The game() function in a program lets a user play a game and returns the score
#    as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
#    contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random
def game():
    print("playing game")
    score=random.randint(1,62)

    with open("hiscore.txt") as f:
        data=f.read()
        if (data!=""):
            hiscore=int(data)
        else:
            hiscore=0
    print(f"hiscore is {hiscore}")  
    print(f"your score is {score}")      
    if (score > hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score
game()
