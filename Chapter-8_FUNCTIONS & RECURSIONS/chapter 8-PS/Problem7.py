# 7). Write a python function to remove a given word from a list ad strip it at the same
#     time.

def remove_word(l,word):
    n=[]
    for i in l:
        if not(i==word):
            n.append(i.strip(word))    #strip method remove word 
    return n

l=["abhi","samA","adi","abhinandan"]
print(remove_word(l,"A"))