"""1) Write a python program that takes in a student name, class.
 It should also take in five subject marks of the students and find the total mark and percentage.
 Display a result in such a way that their name , class and percentage are printed.
"""

student_name = input(" enter your name = " )
student_class = input(" enter your class = " )

student_sub1 = int(input(" enter marks of sub1 = "))
student_sub2 = int(input(" enter marks of sub2 = "))
student_sub3 = int(input(" enter marks of sub3 = "))
student_sub4 = int(input(" enter marks of sub4 = "))
student_sub5 = int(input(" enter marks of sub5 = "))

total_marks = student_sub1+student_sub2+student_sub3+student_sub4+student_sub5
percentage = (total_marks/500)*100

if percentage >= 60:
    print("Grade A")
elif percentage >= 50 and percentage < 60:
    print("Grade B")
elif percentage >= 40 and percentage < 50:
    print("Grade C")
elif percentage >= 33 and percentage < 40:
    print("Grade D")
else :
    print("Fail")

print("student name is =" , student_name , " , class is = " , student_class , f" and percentage is = {percentage:.2f}%")

print("---------------------------------------------------------------------------------------------------------------")

"""
2) Input 2 strings concatinate them and store in another variable.  
then perform generally used string methods on it like """

a = input("enter your first name = ")
b= input("enter your last name = ")
c = a + b

print(c.upper())
print(c.lower())
print(c.center(30))
print(c.capitalize())
print(c.startswith("g"))
print(c.endswith("g"))
print(c.find("k"))
print(c.rfind("u"))
seq=(a,b)
z="_"
print(z.join(seq))

print(c.count("s"))

print(id(c))