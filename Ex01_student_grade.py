# Student Marks, Percentage and Grade
name =input("Enter your name:")
n=int(input("Enter number of subjects:"))
total=0
for i in range(1,n+1):
    mark= float(input(f"Enter mark for subject {i}: "))
    total+=mark
percentage = total/n
if percentage>=90:
    grade = "A+"
    performance = "Outstanding"
elif percentage>=80:
    grade="A"
    performance= "Excellent"
elif percentage>=70:
    grade="B"
    performance="Very Good"
elif percentage>=60:
    grade="C"
    performance = "Good"
elif percentage>=50:
    grade = "D"
    performance = "Average"
else:
    grade="F"
    performance = "Need improvement"
print("\n -----Academic performance-----")
print("Student Name :",name)
print("Total Marks :",total)
print("percentage  :",round(percentage,2), "%")
print("Grade   :",grade)
print("performance :",performance)
    
