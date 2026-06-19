# 5. Repeat program 4 for a list of such words to be censored.

words=["Ram","Sam","Tony"]   #list of words already have in file 

with open("word.txt","r") as f:
    text=f.read()

for word in words:
    text=text.replace(word,"#"* len(word))  #replace the word with #
    #1 word = 1 hash

with open("word.txt","w") as f:
    f.write(text)