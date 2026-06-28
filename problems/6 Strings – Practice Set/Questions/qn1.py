# Write a program that counts how many vowels are in a given string.

string="Coding in Python is fun"
sum=0
vowels="a","e","i","o","u"
for ch in string.lower():
    if (ch in vowels):
        sum+=1
print(sum)
