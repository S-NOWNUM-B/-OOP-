# Задание 1
#
# class Student:
#     def __init__(self, name, group, gpa):
#         self.name = name
#         self._group = group
#         self.__gpa = None
#         self.set_gpa (gpa)
#
#     def get_gpa(self):
#         return self.__gpa
#
#     def set_gpa(self, gpa):
#         if 0 <= gpa <= 4:
#             self.__gpa = gpa
#         else:
#             raise ValueError("GPA должен быть в диапазоне от 0 до 4")
#
# student1 = Student("Алиса", "Б01", 3.8)
# student2 = Student("Борис", "В02", 2.5)
#
# print(student1.name)
# print(student1._group)
# print(student1.get_gpa())
# student1.set_gpa(4.0)
# print(student1.get_gpa())
#
# try:
#     student2.set_gpa(4.5)
# except ValueError as e:
#     print(e)

"""
class Student:
    def __init__(self, name, group, gpa):
        self.name = name
        self._group = group
        self.__gpa = None
        self.set_gpa(gpa)
class Student — объявление класса Student.
def __init__ — конструктор, который вызывается при создании объекта. Он принимает параметры name, group, и gpa.
self.name = name — инициализация публичного атрибута name.
self._group = group — инициализация защищённого атрибута _group.
self.__gpa = None — создание приватного атрибута __gpa, который изначально устанавливается в None.
self.set_gpa(gpa) — вызов метода set_gpa для проверки и установки значения GPA.

def get_gpa(self):
    return self.__gpa
Метод get_gpa возвращает текущее значение приватного атрибута __gpa.

def set_gpa(self, gpa):
    if 0 <= gpa <= 4:
        self.__gpa = gpa
    else:
        raise ValueError("GPA должен быть в диапазоне от 0 до 4.")
Метод set_gpa:
Проверяет, что значение gpa находится в пределах от 0 до 4.
Если значение корректно, записывает его в приватный атрибут __gpa.
Если значение некорректно, выбрасывает исключение ValueError с сообщением.

student1 = Student("Алиса", "Б01", 3.8)
student2 = Student("Борис", "В02", 2.5)
student1 — создаётся объект класса Student с именем "Алиса", группой "Б01" и начальным GPA 3.8. Значение GPA проверяется через метод set_gpa и устанавливается в атрибут __gpa.
student2 — создаётся объект с именем "Борис", группой "В02" и начальным GPA 2.5.

print(student1.name)
Выводит значение публичного атрибута name объекта student1: "Алиса".

print(student1._group)
Выводит значение защищённого атрибута _group объекта student1: "Б01". Несмотря на соглашение о защите, доступ к этому атрибуту извне возможен.

print(student1.get_gpa())
Вызывает метод get_gpa, который возвращает значение приватного атрибута __gpa объекта student1: 3.8.

student1.set_gpa(4.0)
print(student1.get_gpa())
student1.set_gpa(4.0) — изменяет значение GPA на 4.0 через метод set_gpa. Поскольку значение корректно, оно устанавливается.
print(student1.get_gpa()) — выводит обновлённое значение __gpa: 4.0.

try:
    student2.set_gpa(4.5)
except ValueError as e:
    print(e)
student2.set_gpa(4.5) — пытается установить GPA 4.5. Метод set_gpa определяет, что это значение выходит за пределы допустимого диапазона (0–4), и выбрасывает исключение ValueError.
except ValueError as e — перехватывает исключение и выводит сообщение: "GPA должен быть в диапазоне от 0 до 4.".
"""

# Задание 2
#
# class Student:
#     def __init__(self, name, group, gpa):
#         self.name = name
#         self._group = group
#         self.__gpa = None
#         self.set_gpa(gpa)
#
#     def get_gpa(self):
#         return self.__gpa
#
#     def set_gpa(self, gpa):
#         if 0 <= gpa <= 4:
#             self.__gpa = gpa
#         else:
#             raise ValueError("GPA должен быть в диапазоне от 0 до 4")
#
#     def __str__(self):
#         return f"Student: {self.name}, Group: {self._group}, GPA: {self.__gpa:.2f}"
#
# student1 = Student("Алиса", "Б01", 3.8)
# student2 = Student("Борис", "В02", 2.5)
# student3 = Student("Клара", "Г03", 4.0)
#
# print(student1)
# print(student2)
# print(student3)

"""
class Student:
    def __init__(self, name, group, gpa):
        self.name = name
        self._group = group
        self.__gpa = None
        self.set_gpa(gpa)
class Student — объявление класса Student.
def init — конструктор, который вызывается при создании объекта. Он принимает параметры name, group, и gpa.
self.name = name — инициализация публичного атрибута name.
self._group = group — инициализация защищённого атрибута _group.
self.__gpa = None — создание приватного атрибута __gpa, который изначально устанавливается в None.
self.set_gpa(gpa) — вызов метода set_gpa для проверки и установки значения GPA.

def get_gpa(self):
    return self.__gpa
Метод get_gpa:
Возвращает текущее значение приватного атрибута __gpa.

def set_gpa(self, gpa):
    if 0 <= gpa <= 4:
        self.__gpa = gpa
    else:
        raise ValueError("GPA должен быть в диапазоне от 0 до 4")
Метод set_gpa:
Проверяет, что значение gpa находится в диапазоне от 0 до 4.
Если значение корректно, записывает его в приватный атрибут __gpa.
Если значение некорректно, выбрасывает исключение ValueError с сообщением.        

def __str__(self):
    return f"Student: {self.name}, Group: {self._group}, GPA: {self.__gpa:.2f}"
Метод __str__:
Переопределяет строковое представление объекта.
Возвращает строку с информацией о студенте: имя, группа и GPA (с точностью до 2 знаков).

student1 = Student("Алиса", "Б01", 3.8)
student2 = Student("Борис", "В02", 2.5)
student3 = Student("Клара", "Г03", 4.0)
student1: создаётся объект класса Student с именем "Алиса", группой "Б01", и GPA 3.8.
student2: создаётся объект с именем "Борис", группой "В02", и GPA 2.5.
student3: создаётся объект с именем "Клара", группой "Г03", и GPA 4.0.

print(student1)
print(student2)
print(student3)
print(student1):
Вызывает метод __str__ для объекта student1.
Выводит: "Student: Алиса, Group: Б01, GPA: 3.80".
print(student2):
Вызывает метод __str__ для объекта student2.
Выводит: "Student: Борис, Group: В02, GPA: 2.50".
print(student3):
Вызывает метод __str__ для объекта student3.
Выводит: "Student: Клара, Group: Г03, GPA: 4.00".
"""

# Задание 3
#
# class Course:
#     def __init__(self, course_name):
#         self.course_name = course_name
#         self.students = []
#
#     def add_student(self, student):
#         if isinstance(student, Student):
#             self.students.append(student)
#         else:
#             raise TypeError("Можно добавлять только объекты класса Student")
#
#     def __str__(self):
#         student_list = "\n- ".join ([str(student) for student in self.students])
#         return f"Course: {self.course_name}\nStudents:\n- {student_list}" if self.students else f"Course: {self.course_name}\nStudents: None"
#
# student1 = Student("Алиса", "Б01", 3.8)
# student2 = Student("Борис", "В02", 2.5)
# student3 = Student("Клара", "Г03", 4.0)
#
# course = Course ("Объектно ориентированное программирование")
#
# course.add_student(student1)
# course.add_student(student2)
# course.add_student(student3)
#
# print(course)

"""
def __init__(self, course_name):
    self.course_name = course_name
    self.students = []
course_name: Публичный атрибут для названия курса.
students: Список студентов, изначально пустой.

def add_student(self, student):
    if isinstance(student, Student):
        self.students.append(student)
    else:
        raise TypeError("Можно добавлять только объекты класса Student")
Проверяет, что добавляемый объект принадлежит классу Student.
Если это так, добавляет объект в список students.
В противном случае выбрасывает исключение TypeError.

def __str__(self):
    student_list = "\n- ".join([str(student) for student in self.students])
    return f"Course: {self.course_name}\nStudents:\n- {student_list}" if self.students else f"Course: {self.course_name}\nStudents: None"
Формирует строку с информацией о курсе:
Если список студентов пуст, выводит: "Students: None".
Если в списке есть студенты, выводит их строковое представление (__str__ из класса Student) в формате:
"""