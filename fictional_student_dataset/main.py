import csv

# Load and display the fictional student dataset.
with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    students = list(reader)

print(f"Total students: {len(students)}")
print("-" * 90)

for student in students:
    print(
        f"{student['Student ID']:7} | "
        f"{student['Department']:25} | "
        f"Level {student['Level']:3} | "
        f"Attendance: {student['Attendance Percentage']}% | "
        f"Average score: {student['Average Examination Score']}"
    )
