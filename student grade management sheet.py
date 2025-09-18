# student_grade_management.py
def grade_system():
    # Get number of students (with validation)
    while True:
        n_str = input("Enter number of students: ").strip()
        try:
            n = int(n_str)
            if n <= 0:
                print("Please enter a positive integer (e.g., 3).")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer (e.g., 3).")

    records = {}
    for i in range(1, n + 1):
        # Get student name (non-empty)
        name = input(f"Enter name of student #{i}: ").strip()
        while not name:
            name = input("Name cannot be empty. Enter student name: ").strip()

        # Get marks (with validation, allow decimals)
        while True:
            marks_str = input(f"Enter marks for {name}: ").strip()
            try:
                marks = float(marks_str)
                if marks < 0:
                    print("Marks cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid marks. Enter a number like 85 or 72.5.")

        records[name] = marks

    # Print results with Grade mapping
    print("\nStudent Records:")
    for name, marks in records.items():
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "F"
        print(f"{name}: {marks} -> Grade {grade}")


if __name__ == "__main__":
    grade_system()
