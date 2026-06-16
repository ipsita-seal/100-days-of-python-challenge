"""
[OOP]
Create a Student Class
Features:
Name
Roll Number
Marks
Display Details
"""

class Student:
    def __init__(self, name, roll, marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print("Student Name:", self.name)
        print("Student Roll Number:", self.roll)
        print("Marks obtained: ", self.marks)

name = input("enter name: ")
roll = int(input("enter roll: "))
marks = float(input("enter marks: "))
A = Student(name, roll, marks)
A.display()
