class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def student_name(self):
        return f"Student Name : {self.name}"

    @property
    def student_mark(self):
        return f"Student Mark Percentage : {self.marks}"


def mark_percent():
    total_mark = 0
    for i in range(1, 6):
        subject_mark = int(input(f"Enter Subject {i} mark : "))
        total_mark += subject_mark
    avg_mark = total_mark / 5
    return avg_mark


stu_name = input("Enter the student name : ")
stu_marks = mark_percent()
student_1 = Student(stu_name, stu_marks)

print(student_1.student_name)
print(student_1.student_mark)

# student_1.student_name = "ginger"