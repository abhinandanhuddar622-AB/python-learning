print("lower and upper....")
name="Abhi"
print(name.lower())  # string convert into the lower case 
print(name.upper())  # full word capital

print("title....")
text="hello world"
print(text.title())   #first letter of each word capital

print("capitalize....")
print(text.capitalize())   # only first letter capital 

print("islower and isupper....")
print(name.islower())   #check string is lower or not
print(name.isupper())   #check string is upper or not

print("startswith and endswith....")
text1="hello world"
print(text1.startswith("hello"))   #check string start with hello or not

text2="hello world"
print(text2.endswith("world"))   #check string end with world or not

print("strip....")
text2=" hello world "
print(text2.strip())   #remove space from start and end

print("lstrip....")
text2=" hello world "
print(text2.lstrip())   #remove space from start

print("rstrip....")
text2=" hello world "
print(text2.rstrip())   #remove space from end

print("replace....")
text2=" hello world "
print(text2.replace("hello world","hi"))

print("split....")
text4="Apple,Mango,Banana"
print(text4.split(","))  #convert string into list

print("join....")
fruits = ['apple', 'banana', 'mango']
print(",".join(fruits))  #convert list into string

print("find....")
text = "python programming"
print(text.find("pro"))   # 7 is pro index

print("count....")
text = "python programming"
print(text.count("pro"))   # 1 is pro count
print(text.count("m"))   # 2 is m count

print("index....")
text = "python programming"
print(text.index("pro"))   # 7 is pro index

print("startswith....")
text = "python"
print(text.startswith("py"))   # True 

print("endswith....")
text = "python"
print(text.endswith("on"))   # True

print("isdigit....")
t="123"
print("123".isdigit())   # True
print(t.isdigit())

print("isalpha....")
print("abc".isalpha())   # True

print("isalnum....")
print("Abhi123".isalnum())   # True
print("A@".isalnum())