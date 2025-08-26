'''Q4. Write a program to calculate the grade of a student. There are five 
subjects. Marks in each subject are entered from keyboard. Assign grade 
based on the following rule:
Total Marks >= 90 Grade: Ex
90 > Total Marks >= 80 Grade: A
80 > Total Marks >= 70 Grade: B
70 > Total Marks >= 60 Grade: C
60 > Total Marks Grade: F'''


total = 0
subjects = 5
for i in range(subjects):
    m = int(input(f"Enter marks for subject {i+1}: "))
    total += m

if total >= 90:
    grade = "Ex"
elif total >= 80:
    grade = "A"
elif total >= 70:
    grade = "B"
elif total >= 60:
    grade = "C"
else:
    grade = "F"

print("Total Marks:", total)
print("Grade:", grade)
