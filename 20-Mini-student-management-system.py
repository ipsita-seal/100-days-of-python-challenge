#Mini Student Management System
"""
Features:
Add Student
View Students
Search Student
Delete Student
"""
student_database = []
def add_student(student_database):
  id = int(input("Enter student id:"))
  name = input("Enter Name: ")
  age = int(input("Enter Age: "))
  course = input("Enter Course: ")
  student = {
      "ID": id,
      "NAME": name,
      "AGE": age,
      "COURSE": course
  }
  student_database.append(student)
  print("\nStudent added successfully")
  def view_student(student_database):
  if len(student_database) == 0:
        print("\nNo records found")
        return
  for i in student_database:
    print(i)
    def search_student(student_database):
  id = int(input("Enter student id:"))
  for i in student_database:
    if i["ID"] == id:
      return i
  return "Student not found"
  def delete_student(student_database):
  id = int(input("Enter ID of student to delete record: "))
  for i in student_database:
    if i["ID"]==id:
      student_database.remove(i)
      print("\nStudent deleted successfully")
      return
  print("\nStudent not found")
  while True:
  print("\nEnter 1 to add student")
  print("Enter 2 to view student")
  print("Enter 3 to search student")
  print("Enter 4 to delete student")
  print("Enter 5 to exit\n")

  choice = int(input("Enter your choice: "))
  if choice == 1:
    add_student(student_database)
  elif choice == 2:
    view_student(student_database)
  elif choice == 3:
    print(search_student(student_database))
  elif choice == 4:
    delete_student(student_database)
  elif choice == 5:
    print("Exited successfully")
    break
  else:
    print("\nInvalid choice\n")
