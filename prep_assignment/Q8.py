'''Q8. Write a program to read the name of a student (studentName), roll 
Number (rollNo) and marks (totalMarks) obtained. rollNo may be an 
alphanumeric string. Display the data as read. Hint: Create a Student 
structure and write appropriate functions.'''


class Student:
    def __init__(self, studentName, rollNo, totalMarks):
        self.studentName = studentName
        self.rollNo = rollNo
        self.totalMarks = totalMarks

    def display(self):
        print("Student Name:", self.studentName)
        print("Roll Number:", self.rollNo)
        print("Total Marks:", self.totalMarks)

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = int(input("Enter total marks: "))

s = Student(name, roll, marks)
print("Student Data:")
s.display()
