# 6. Write a program to calculate the grade of a student from his marks from the
#    following scheme:
#    90 – 100 => Ex
#    80 – 90 => A
#    70 – 80 => B
#    60 – 70 =>C
#    50 – 60 => D
#    <50 => F

marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):             #check marks is less than 100 and greater than 90
    grade = "Ex"
elif(marks<90 and marks>=80):             #check marks is less than 90 and greater than 80
    grade = "A"
elif(marks<80 and marks>=70):             #check marks is less than 80 and greater than 70
    grade = "B"
elif(marks<70 and marks>=60):             #check marks is less than 70 and greater than 60
    grade = "C"
elif(marks<60 and marks>=50):             #check marks is less than 60 and greater than 50
    grade = "D"
elif(marks<50):                           #check marks is less than 50
    grade = "F"

print("Your grade is:", grade)