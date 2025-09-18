# 🎓 Student Grade Management System (Python)

Author : M.S.MEYSINTHA

A simple Python program to manage student grades.

It allows the user to:

Enter multiple student names and marks

Assign grades based on marks

Display a formatted report of all students

# 📌 Features

✅ Input any number of students
✅ Automatic grade calculation:

Marks ≥ 90 → Grade A

Marks ≥ 75 → Grade B

Marks ≥ 50 → Grade C

Marks < 50 → Grade F
✅ Input validation for numbers, names, and marks
✅ Beginner-friendly and easy to extend

# 📜 Code Example
def grade_system():
    n = int(input("Enter number of students: "))
    records = {}

    for _ in range(n):
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        records[name] = marks

    print("\nStudent Records:")
    for name, marks in records.items():
        grade = "A" if marks >= 90 else "B" if marks >= 75 else "C" if marks >= 50 else "F"
        print(f"{name}: {marks} -> Grade {grade}")

grade_system()

# ▶️ Example Run
Enter number of students: 3
Enter student name: Meysintha
Enter marks: 92
Enter student name: Alice
Enter marks: 78.5
Enter student name: Bob
Enter marks: 45

Student Records:
Meysintha: 92.0 -> Grade A
Alice: 78.5 -> Grade B
Bob: 45.0 -> Grade F

# ⚡ How to Run

Clone this repository:

git clone https://github.com/your-username/student-grade-management.git
cd student-grade-management


# Run the program:

python student_grade_management.py

# output



# 🚀 Future Improvements

Save student records in a CSV/Excel file

Allow updating/deleting student records

Add a GUI (Tkinter/Streamlit) for better usability
