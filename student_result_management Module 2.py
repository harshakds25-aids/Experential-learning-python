class Student:

    def __init__(self, roll_no, name, course, semester, marks):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.semester = semester
        self.marks = marks

    def calculate_total(self):
        pass

    def calculate_percentage(self):
        pass

    def calculate_grade(self):
        pass

    def get_status(self):
        pass

    def to_dict(self):
        pass


class ResultManagementSystem:

    FILE_NAME = "students.json"

    def __init__(self):
        self.students = {}
        self.load_data()

    def load_data(self):
        pass

    def save_data(self):
        pass

    def add_student(self):
        pass

    def view_students(self):
        pass

    def search_student(self):
        pass

    def display_result(self, student):
        pass

    def update_student(self):
        pass

    def delete_student(self):
        pass

    def generate_report(self):
        pass
