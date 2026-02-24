# Program 6: Student Marks and Grade Calculator
# This program takes marks of five subjects as input, calculates 
# total marks, percentage, assigns a grade, and determines pass/fail status.

# Taking input marks for five subjects
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

# Calculating total marks
sum_marks = m1 + m2 + m3 + m4 + m5

# Calculating percentage
percent = sum_marks / 5

# Assigning grade based on percentage
if percent >= 90:
    grade_value = "A+ (Outstanding)"
elif percent >= 80:
    grade_value = "A (Excellent)"
elif percent >= 70:
    grade_value = "B (Good)"
elif percent >= 60:
    grade_value = "C (Average)"
elif percent >= 50:
    grade_value = "D (Pass)"
else:
    grade_value = "F (Fail)"

# Determining pass/fail condition (must score at least 40 in each subject)
if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
    final_status = "Pass"
else:
    final_status = "Fail"

# Displaying student report
print("\nSTUDENT REPORT")
print("Marks entered:", m1, m2, m3, m4, m5)
print("Total marks obtained:", sum_marks)
print("Overall percentage:", round(percent, 2), "%")
print("Grade received:", grade_value)
print("Result status:", final_status)