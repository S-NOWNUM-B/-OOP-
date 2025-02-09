# Задание 1
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def addBook(self, book):
#         self.books.append(book)
#
#     def __len__(self):
#         return len(self.books)
#
#     def __getitem__(self, index):
#         return self.books[index]
#
#     def __str__(self):
#         return str(self.books)
#
#
# class DigitalLibrary(Library):
#     def __init__(self):
#         super().__init__()
#         self.ebooks = []
#
#     def addBook(self, book, digital=False):
#         if digital:
#             self.ebooks.append(book)
#         else:
#             super().addBook(book)
#
#     def __repr__(self):
#         return f"Обычные книги - {', '.join(self.books) if self.books else 'нет'}!\n" \
#                f"Электронные книги - {', '.join(self.ebooks) if self.ebooks else 'нет'}!"
#
#
# lib = Library()
# digital_lib = DigitalLibrary()
#
# lib.addBook("1984")
# lib.addBook("Автостопом по галактике")
# lib.addBook("Путешествие на запад")
#
# digital_lib.addBook("Сияние", digital=True)
# digital_lib.addBook("Зов Ктулху", digital=True)
# digital_lib.addBook("Ведьмак", digital=True)
# digital_lib.addBook("Гарри Поттер", digital=False)
# digital_lib.addBook("Гроздья Гнева", digital=False)
#
# print(lib.books)
# print(digital_lib.ebooks)
#
# print(len(lib))
# print(lib[0])
# print(str(lib))
#
# print(repr(digital_lib))
#
# Задание 2
#
# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
#
#     def addItem(self, item, quantity=1):
#         if item in self.items:
#             self.items[item] += quantity
#         else:
#             self.items[item] = quantity
#
#     def __len__(self):
#         return sum(self.items.values())
#
#     def __getitem__(self, item):
#         return self.items.get(item, 0)
#
#     def __call__(self):
#         return self.items
#
# shop = ShoppingCart()
#
# shop.addItem("Яблоко", 1)
# shop.addItem("Банан", 32)
# shop.addItem("Макароны", 5)
#
# print(shop.items)
# print(len(shop))
# print(shop["Банан"])
# print(shop())
#
# Задание 3
#
# class Polynomial:
#     def __init__(self, coefficients):
#         self.coefficients = coefficients
#
#     def __str__(self):
#         terms = []
#         for power, coef in enumerate(self.coefficients):
#             if coef == 0:
#                 continue
#             if power == 0:
#                 terms.append(f"{coef}")
#             elif power == 1:
#                 terms.append(f"{coef}x")
#             else:
#                 terms.append(f"{coef} x^ {power}")
#         return " + ".join(terms[::-1]) or "0"
#
#     def __repr__(self):
#         return f"Polynomial({self.coefficients})"
#
#     def __add__(self, other):
#         max_len = max(len(self.coefficients), len(other.coefficients))
#         new_coeffs = [0] * max_len
#         for i in range(max_len):
#             a = self.coefficients[i] if i < len(self.coefficients) else 0
#             b = other.coefficients[i] if i < len(other.coefficients) else 0
#             new_coeffs[i] = a + b
#         return Polynomial(new_coeffs)
#
#     def __getitem__(self, degree):
#         return self.coefficients[degree] if degree < len(self.coefficients) else 0
#
# p1 = Polynomial([2, 0, 3])
# p2 = Polynomial([1, 4, 0, 5])
#
# print(p1)
# print(p2)
#
# p3 = p1 + p2
# print(p3)
#
# print(p1[2])
# print(p1[5])
#
# print(repr(p1))