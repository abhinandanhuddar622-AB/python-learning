def myfun():
    print("Hello Abhi")

if __name__=="__main__":
#if this code is directly executed by running the file its present in 

# the below code is not run in main file 
    #BCS __name__=="__main__"
    #only run in this file 
    
    print("we  are directly running this code")
    myfun()
    print(__name__)

    # the above code is not run in main file 
    #BCS __name__=="__main__"