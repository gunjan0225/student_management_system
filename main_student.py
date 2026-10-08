# ==========================================
# STUDENT MANAGEMENT SYSTEM
# ==========================================

students = []

# ------------------------------------------
# Function to calculate percentage
# ------------------------------------------

def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return total, percentage

# ------------------------------------------
# Function to calculate grade
# ------------------------------------------

def calculate_grade(percentage):
  if percentage >= 90:
    return "A+"
  elif percentage >= 80:
    return "A"
  elif percentage >= 70:
    return "B"
  elif percentage >= 60:
    return "C"
  elif percentage >= 50:
    return "D"
  elif percentage >= 40:
    return "E"
  else:
    return "F"

# ------------------------------------------
# Function to check pass/fail
# ------------------------------------------

def check_result(marks):
  for mark in marks:
    if mark < 40:
      return "Fail"

  return "Pass"

# ------------------------------------------
# Add Student
# ------------------------------------------

def add_student():
    print("\n========== ADD STUDENT ==========")

    roll = int(input("Enter Roll Number: "))

    # Check duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Student with this roll number already exists.")
            return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    print("\nEnter marks for 5 subjects:")

    marks = []

    for i in range(1, 6):
        while True:
            mark = float(input(f"Enter marks for Subject {i}: "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks must be between 0 and 100.")

    total, percentage = calculate_percentage(marks)

    grade = calculate_grade(percentage)
    result = check_result(marks)

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result,
    }

    students.append(student)

    print("\nStudent added successfully!")

# ------------------------------------------
# Display One Student
# ------------------------------------------

def display_student(student):
    print("\n------------------------------------------")
    print("Roll Number :", student["roll"])
    print("Name        :", student["name"])
    print("Age         :", student["age"])
    print("Course      :", student["course"])
    print("Marks       :", student["marks"])
    print("Total       :", student["total"])
    print("Percentage  :", round(student["percentage"], 2))
    print("Grade       :", student["grade"])
    print("Result      :", student["result"])
    print("------------------------------------------")

# ------------------------------------------
# Display All Students
# ------------------------------------------

def display_all_students():
    print("\n========== ALL STUDENTS ==========")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        display_student(student)

# ------------------------------------------
# Search Student
# ------------------------------------------

def search_student():
    print("\n========== SEARCH STUDENT ==========")

    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:
            display_student(student)
            return

    print("Student not found.")

# ------------------------------------------
# Update Student
# ------------------------------------------

def update_student():

    print("\n========== UPDATE STUDENT ==========")
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found")
            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Course")
            print("4. Update Marks")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                student["name"] = input("Enter new name: ")
                print("Name updated successfully.")
            elif choice == 2:
                student["age"] = int(input("Enter new age: "))
                print("Age updated successfully.")
            elif choice == 3:
                student["course"] = input("Enter new course: ")
                print("Course updated successfully.")
            elif choice == 4:
                print("\nEnter new marks:")
                marks = []
                for i in range(1, 6):
                    while True:
                        mark = float(input(f"Enter marks for Subject {i}: "))
                        if 0 <= mark <= 100:
                            marks.append(mark)
                            break
                        print("Marks must be between 0 and 100.")
                student["marks"] = marks
                total, percentage = calculate_percentage(marks)
                student["total"] = total
                student["percentage"] = percentage
                student["grade"] = calculate_grade(percentage)
                student["result"] = check_result(marks)
                print("Marks updated successfully.")
            else:
                print("Invalid choice.")
            return

    print("Student not found.")

# ------------------------------------------
# Delete Student
# ------------------------------------------
def delete_student():
  print("\n========== DELETE STUDENT ==========")

  roll = int(input("Enter Roll Number: "))

  for student in students:
    if student["roll"] == roll:
      confirmation = input(
        "Are you sure you want to delete this student? (yes/no): "
      )
      if confirmation.lower() == "yes":
        students.remove(student)
        print("Student deleted successfully.")
      else:
        print("Deletion cancelled.")
      return

  print("Student not found.")

# ------------------------------------------
# Display Result
# ------------------------------------------

def display_result():
  print("\n========== STUDENT RESULT ==========")
  roll = int(input("Enter Roll Number: "))

  for student in students:
    if student["roll"] == roll:
      print("\nStudent Name:", student["name"])
      print("Roll Number:", student["roll"])
      print("\nSubject-wise Marks:")
      for i, mark in enumerate(student["marks"], 1):
        print("Subject", i, ":", mark)
      print("\nTotal Marks:", student["total"])
      print("Percentage:", round(student["percentage"], 2))
      print("Grade:", student["grade"])
      print("Result:", student["result"])
      return

  print("Student not found.")

# ------------------------------------------
# Find Topper
# ------------------------------------------

def find_topper():
  print("\n========== CLASS TOPPER ==========")
  if len(students) == 0:
    print("No students found.")
    return
  topper = max(students, key=lambda student: student["percentage"])
  print("\nClass Topper:")
  display_student(topper)

# ------------------------------------------
# Display Passed Students
# ------------------------------------------

def display_passed_students():
    print("\n========== PASSED STUDENTS ==========")
    found = False

    for student in students:
        if student["result"] == "Pass":
            display_student(student)
            found = True

    if not found:
        print("No student has passed.")

# ------------------------------------------
# Display Failed Students
# ------------------------------------------

def display_failed_students():
    print("\n========== FAILED STUDENTS ==========")
    found = False

    for student in students:
        if student["result"] == "Fail":
            display_student(student)
            found = True

    if not found:
        print("No student has failed.")

# ------------------------------------------
# Sort Students
# ------------------------------------------
def sort_students():
    print("\n========== SORT STUDENTS ==========")
    if len(students) == 0:
        print("No students found.")
        return
    sorted_students = sorted(
        students,
        key=lambda student: student["percentage"],
        reverse=True,
    )
    print("\nStudents sorted by percentage:\n")
    for student in sorted_students:
        print(
            student["roll"], "-", student["name"],
            "-", round(student["percentage"], 2), "%"
        )

# ------------------------------------------
# Count Students
# ------------------------------------------

def count_students():

  print("\n========== STUDENT COUNT ==========")

  total = len(students)

  passed = 0
  failed = 0

  for student in students:

    if student["result"] == "Pass":
      passed += 1
    else:
      failed += 1

  print("Total Students :", total)
  print("Passed Students:", passed)
  print("Failed Students:", failed)

# ------------------------------------------
# Main Menu
# ------------------------------------------

while True:
  print("\n==========================================")
  print("       STUDENT MANAGEMENT SYSTEM")
  print("==========================================")
  print("1. Add Student")
  print("2. Display All Students")
  print("3. Search Student")
  print("4. Update Student")
  print("5. Delete Student")
  print("6. Display Result")
  print("7. Find Class Topper")
  print("8. Display Passed Students")
  print("9. Display Failed Students")
  print("10. Sort Students by Percentage")
  print("11. Count Students")
  print("12. Exit")
  print("==========================================")

  choice = input("Enter your choice: ")
  if choice == "1":
    add_student()
  elif choice == "2":
    display_all_students()
  elif choice == "3":
    search_student()
  elif choice == "4":
    update_student()
  elif choice == "5":
    delete_student()
  elif choice == "6":
    display_result()
  elif choice == "7":
    find_topper()
  elif choice == "8":
    display_passed_students()
  elif choice == "9":
    display_failed_students()
  elif choice == "10":
    sort_students()
  elif choice == "11":
    count_students()
  elif choice == "12":
    print("\nThank you for using Student Management System!")
    break
  else:
    print("Invalid choice. Please try again.")