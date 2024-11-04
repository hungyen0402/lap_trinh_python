class Student:
    def __init__(self, student_id, name, class_name):
        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.attendance_record = ""

    def set_attendance(self, attendance):
        self.attendance_record = attendance

    def calculate_attendance_score(self):
        score = 10  # Điểm tối đa
        absences = self.attendance_record.count('v')
        tardies = self.attendance_record.count('m')
        score -= (absences * 2) + tardies
        return max(score, 0)  # Đảm bảo điểm không âm

    def __str__(self):
        score = self.calculate_attendance_score()
        if score == 0:
            return f"{self.student_id} {self.name} {self.class_name} {score} KDDK"
        else:
            return f"{self.student_id} {self.name} {self.class_name} {score}"


class AttendanceSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def input_attendance(self, student_id, attendance):
        for student in self.students:
            if student.student_id == student_id:
                student.set_attendance(attendance)

    def display_results(self):
        for student in self.students:
            print(student)


if __name__ == '__main__':
    n = int(input().strip())  # Số sinh viên
    attendance_system = AttendanceSystem()

    # Nhập thông tin sinh viên
    for _ in range(n):
        student_id = input().strip()  # Mã sinh viên
        name = input().strip()         # Họ tên
        class_name = input().strip()   # Lớp
        student = Student(student_id, name, class_name)
        attendance_system.add_student(student)

    # Nhập dữ liệu điểm danh
    for _ in range(n):
        record = input().strip().split()
        student_id = record[0]
        attendance = record[1]
        attendance_system.input_attendance(student_id, attendance)

    # In kết quả
    attendance_system.display_results()
