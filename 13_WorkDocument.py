class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student(ID={self.student_id}, Name='{self.name}', Grade={self.grade})"

def linear_search_by_name(students, target_name):
    for student in students:
        if student.name == target_name:
            return student
    return None

def binary_search_by_id(students, target_id):
    students_sorted = sorted(students, key=lambda s: s.student_id)
    left = 0
    right = len(students_sorted) - 1
    while left <= right:
        mid = (left + right) // 2
        if students_sorted[mid].student_id == target_id:
            return students_sorted[mid]
        elif students_sorted[mid].student_id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return None

students = [
    Student(3, "Alice", 85),
    Student(1, "Bob", 90),
    Student(5, "Charlie", 75),
    Student(2, "David", 95),
    Student(4, "Eve", 80),
    Student(6, "Frank", 90),
    Student(8, "Stas", 70)
]

print("Линейный поиск 'Stas':")
print(linear_search_by_name(students, "Stas"))

print("\nБинарный поиск ID=2:")
print(binary_search_by_id(students, 2))