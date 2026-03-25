# 7). Write a program to find out whether a given post is talking about “Abhi” or not.

post = input("Enter the post: ")

#if type in post capital or small all work 
if("abhi" in post.lower()):                #post.lower() convert post into the lower case
#if ("Abhi".lower() in post.lower()):    #other method
    print("This post is talking about Abhi")

else:
    print("This post is not talking about Abhi")