"""
Question19 - Attendance Register

Read student names, line by line, from a file.
For each name, ask if the student is in class.
E.g. Is Bisi in class? [yes/no]
Let the user input either yes or no.
"""


def attendance_register():
    with open("attendance.txt", "w") as blank_output_sheet:
        blank_output_sheet.write("")
    with open('student_names.txt', 'r') as students:
        student_names = students.readlines()
        for student in student_names:
            check = input(f"Is {student.strip().capitalize()} in Class? [yes/no]  ").strip().lower()
            if check == "no":
                with open('attendance.txt', 'a') as attendance:
                    attendance.write(f"{student.strip().capitalize().ljust(15)}\t\t❌\n")
            else:
                with open('attendance.txt', 'a') as attendance:
                    attendance.write(f"{student.strip().capitalize().ljust(15)}\t\t✅\n")


if __name__ == '__main__':
    attendance_register()
