"""
    Классы

        Класс - в ООП, модель для создания объектов определённого типа, описывающая их
        структуру и определяющая алгоритмы для работы с этими объектами.

    Пример:

        Класс: Машина
        Объект: Audi, Nissan, Volvo

    Ключевое слово - class
"""

# class Work:
#     def __init__(self):
#         text = input("Введите значение 1 или 73 - ")
#         if text == "1":
#             print("Вы выбралис тандартное число. Не плохо, но второй вариант куда интересней!")
#         else:
#             print("Поздравляю, вы знаток! Говоря о своём любимым числе, Шелдон поясняет: «73 — это 21-е простое число. Написанное наоборот оно 37 — это 12-е простое число, и если написать его наоборот — 21, — это результат умножения семи и трёх, а также число 73, написанное в двоичной системе счисления является палиндромом: 1-0-0-1-0-0-1».")
#
# Work()

# Процедурный код

# n = 20
# fibo = [1,1]
#
# for i in range(1, n):
#     x = fibo[i] + fibo[i-1]
#     fibo.append(x)
#
# print(len(fibo))
# print(fibo)

# Код в виде класса

# class Fibonacci:
#     def __init__(self, n):
#         self.n = n
#         self.fibo = [0, 1]
#
#         self.fill()
#
#     def fill(self):
#         for i in range(1, self.n + 1):
#             self.fibo.append(self.compute(i))
#
#     def compute(self, index):
#         return self.fibo[index - 1] + self.fibo[index - 2]
#
#
# fibonacci = Fibonacci(41)
# print(fibonacci.fibo[-1])

# string = str(input("Введите слово - "))
# integer = int(input("Введите целое число - "))
# float_res = float(input("Введите число с плавающей точкой - "))
#
# print(f"Переменная string = {string}, имеет тип {type(string).__name__}")
# print(f"Переменная integer = {integer}, имеет тип {type(integer).__name__}")
# print(f"Переменная float_res = {float_res}, имеет тип {type(float_res).__name__}")

# first = float(input("Введите первое целое значение или значение с плавающей точкой - "))
# second = float(input("Введите второе целое значение или значение с плавающей точкой - "))
#
# print(f"Результат сложения равен - {first + second}")
# print(f"Результат вычитания равен - {first - second}")
# print(f"Результат умножения равен - {first * second}")
# if second != 0:
#     print(f"Результат деления равен - {second / first}")
#     print(f"Результат целочисленного деления - {second // first}")
#     print(f"Результат остаточного деления - {second % first}")
# else:
#     print(f"Делить на 0 нельзя")
#
# if first > second:
#     print(f"Значение {first} больше чем {second}")
# elif first < second:
#     print(f"Значение {second} больше чем {first}")
# else:
#     print("Значения равны")

# age = int(input("Укажите свой возраст - "))
#
# if 0 <= age <= 12:
#     print("Вы ребёнок")
# elif 13 <= age <= 19:
#     print("Вы подросток")
# elif 20 <= age:
#     print("Вы взрослый")
# else:
#     print("Вы указали неверный возраст")

# number = 20
# fibo = [1,1]
#
# for i in range(1, number):
#     x = fibo[i] + fibo[i-1]
#     fibo.append(x)
#
# print(fibo)