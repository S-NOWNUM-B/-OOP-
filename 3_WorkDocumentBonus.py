# Задание 1
#
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self._author = author
#         self.__price = price
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self, new_price):
#         if new_price > 0:
#             self.__price = new_price
#         else:
#             print("Цена должна быть больше 0")
#
# book1 = Book("1984", "George Orwell", 19.99)
# book2 = Book("To kill a Mockingbird", "Harper Lee", 14.99)
#
# print(book1.title)
# print(book1.get_price())
#
# book1.set_price(22.99)
# print(book1.get_price())
#
# book1.set_price(-10)

"""
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self._author = author
        self.__price = price
class Book — объявление класса Book.
def __init__ — конструктор, вызываемый при создании объекта.
self.title = title — инициализация публичного атрибута title.
self._author = author — инициализация защищённого атрибута _author.
self.__price = price — инициализация приватного атрибута __price.

def get_price(self):
    return self.__price
def get_price(self) — метод, который возвращает значение приватного атрибута __price.
return self.__price — возвращает текущую стоимость книги.

def set_price(self, new_price):
    if new_price > 0:
        self.__price = new_price
    else:
        print("Цена должна быть больше 0")
def set_price(self, new_price) — метод для изменения значения приватного атрибута __price.
if new_price > 0: — проверка, что новая цена больше 0.
self.__price = new_price — если условие выполнено, цена обновляется.
else: — если условие не выполнено, выполняется следующий блок.
print("Цена должна быть больше 0") — вывод сообщения об ошибке, если переданная цена меньше или равна 0.

book1 = Book("1984", "George Orwell", 19.99)
book2 = Book("To kill a Mockingbird", "Harper Lee", 14.99)
Создаются два объекта класса Book:
book1: книга с названием “1984”, автором George Orwell и ценой 19.99.
book2: книга с названием “To kill a Mockingbird”, автором Harper Lee и ценой 14.99.
"""

# Задание 2
#
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self._author = author
#         self.__price = price
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self, new_price):
#         if new_price > 0:
#             self.__price = new_price
#         else:
#             print("Цена должна быть больше 0")
#
#     def __str__(self):
#         return f"Book: {self.title}, Author: {self._author}, Price: {self.__price:.2f}"
#
# book1 = Book("1984", "George Orwell", 19.99)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 14.99)
#
# print(book1)
# print(book2)

"""
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self._author = author
        self.__price = price
class Book — объявление класса Book.
def init — конструктор, вызываемый при создании объекта.
self.title = title — инициализация публичного атрибута title.
self._author = author — инициализация защищённого атрибута _author.
self.__price = price — инициализация приватного атрибута __price.

def get_price(self):
    return self.__price
def get_price(self) — метод, возвращающий значение приватного атрибута __price.
return self.__price — возвращает текущую цену книги.

def set_price(self, new_price):
    if new_price > 0:
        self.__price = new_price
    else:
        print("Цена должна быть больше 0")
def set_price(self, new_price) — метод для изменения цены книги.
if new_price > 0: — проверка, что цена больше 0.
self.__price = new_price — обновление цены, если условие выполнено.
else: — выполняется, если новая цена не соответствует условию.
print(“Цена должна быть больше 0”) — сообщение об ошибке.

def __str__(self):
    return f"Book: {self.title}, Author: {self._author}, Price: {self.__price:.2f}"
def str(self) — метод, возвращающий строку с описанием книги.
return f”…” — возвращает строку формата: название, автор и цена книги.

book1 = Book("1984", "George Orwell", 19.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 14.99)
book1 = Book(…) — создание объекта book1 с указанными параметрами.
book2 = Book(…) — создание объекта book2 с другими параметрами.

print(book1)
print(book2)
print(book1) — вывод информации о книге book1 с помощью метода __str__.
print(book2) — вывод информации о книге book2 с помощью метода __str__.
"""