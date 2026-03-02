def save_to_file(students, filename="students.txt"):
    with open(filename, "w") as file:
        for student in students:
            file.write(f"Name: {student['name']}, Student ID: {student['student_id']}, Favorite AI Tool: {student['favorite_AI_tool']}\n")

students = []

while True:
    print("\nEnter student details:")
    name = input("Name: ")
    student_id = input("Student ID: ")
    favorite_AI_tool = input("Favorite AI Tool: ")

    student = {
        "name": name,
        "student_id": student_id,
        "favorite_AI_tool": favorite_AI_tool
    }

    students.append(student)

    more = input("Add another student? (yes/no): ").lower()
    if more != "yes":
        break

print(f"\nTotal number of students: {len(students)}")
for idx, student in enumerate(students, start=1):
    print(f"{idx}. Name: {student['name']}")
    print(f"   Student ID: {student['student_id']}")
    print(f"   Favorite AI Tool: {student['favorite_AI_tool']}")

save_to_file(students)
print("Student data saved to students.txt")