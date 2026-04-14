f=open("more_file.txt","r")
line1=f.readline()          #read line 1 
line2=f.readline()          
line3=f.readline()
print(line1,type(line1))   #print line 1
print(line2,type(line2))   #print line 2 
print(line3,type(line3))   #line 3 is empty 
f.close()

#a append mode
wr= "Hey Abhi you are amazing"
f=open("file.txt","a")      #a means append 
f.write(wr)
f.close()

# append mode is used to add data to the end of the file
