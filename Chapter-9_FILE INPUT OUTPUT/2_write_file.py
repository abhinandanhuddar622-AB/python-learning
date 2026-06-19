wr= "Hey Abhi you are amazing"
f=open("file.txt","w")      #w means write
f.write(wr)
f.close()


f=open("file.txt","r")     #r means read                  
data=f.read()
print(data)
f.close()