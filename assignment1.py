'''
1) Write a python program that takes in a student name, class. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class,  and percentage are printed.

'''
print("====welcome to the system====")

#details input
name = input("enter the name: ")
Class = int(input("enter the year: "))

# subject marks input
marks = []
for i in range(5):
    mark = int(input(f"enter the mark of subject {i+1}: "))
    marks.append(mark)
# total and percentage calculation
total = sum(marks) 
percentage = (total / 500) * 100

# result display
print(f"Name: {name}")
print(f"Class: {Class}")
print(f"Percentage: {percentage:.2f}%")

#alternative method
print("welcome to the system")

name = input("enter the name")
Class = int(input("enter the year:"))

maths = int(input("enter the marks for maths:"))
cam = int(input("enter the marks for cam:"))
dsa = int(input("enter the marks for dsa :"))
fods = int(input("enter the marks for fods :"))
os = int(input("enter the marks for os:"))

total = maths + cam  + dsa + fods + os
percentage_student = (total/500)*100

print("-----Student Details-----")
print(f"Student name: {name}")
print(f"collage year: {Class}")
print(f"percentage : {percentage_student:.2f}%")

'''
 Input 2 strings concatinate them and store in another variable. then perform generally used string methods on it like

lower(), upper(), title(), swapcase(), capitalize(), casefold(), center(), count(), endswith(), find(), isalnum(), isdigit(), isnumeric(), isspace(), replace()
'''