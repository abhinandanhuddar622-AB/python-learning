# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
#    different files. Place these files in a folder for a 13 – year old.

def generatables(n):
    table=""             #table is empty
    for i in range (1,11):   #i=1 to 10
        table+=f"{n} x {i} = {n*i}\n"  #formula for multiplication
    
    with open (f"tables/table_{n}.txt","w") as f:   
        #create a new file as table_2.txt
        f.write(table)

for i in range(2,21):         #i=2 to 20,20 is last tables
    generatables(i)