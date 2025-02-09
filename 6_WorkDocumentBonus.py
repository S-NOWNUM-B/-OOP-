# Класс Library представляет обычную библиотеку с физическими книгами
class Library:
    def __init__(self):
        self.books = []  # Список для хранения книг

    def addBooks(self, book):
        self.books.append(book)  # Добавляем книгу в библиотеку

    def __len__(self):
        return len(self.books)  # Позволяет использовать len() для подсчета книг

    def __getitem__(self, index):
        return self.books[index]  # Позволяет получать книги по индексу

    def __str__(self):
        return ", ".join(self.books) if self.books else "Библиотека пуста"
        # Возвращает строку с книгами, если библиотека не пуста

# Класс DigitalLibrary расширяет Library, добавляя поддержку электронных книг
class DigitalLibrary(Library):
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса
        self.ebooks = []  # Отдельный список для хранения электронных книг

    def addBooks(self, book, digital=False):
        if digital:  # Если передан флаг digital=True, добавляем в электронную библиотеку
            self.ebooks.append(book)
        else:  # Иначе добавляем в обычные книги
            self.books.append(book)

    def __repr__(self):
        # Красивый вывод информации о библиотеке (обычные и электронные книги)
        return f'Обычные книги: {", ".join(self.books) if self.books else "нет"}!\n' \
               f'Электронные книги: {", ".join(self.ebooks) if self.ebooks else "нет"}!'

# Создаем экземпляр цифровой библиотеки
library = DigitalLibrary()

# Добавляем обычную книгу
library.addBooks("1984")

# Добавляем электронную книгу
library.addBooks("Brave New World", digital=True)

# Добавляем еще одну обычную книгу
library.addBooks("Fahrenheit 451")

# Добавляем еще одну электронную книгу
library.addBooks("Digital Fortress", digital=True)

# Выводим количество обычных книг (len считает только физические книги!)
print(len(library))  # Ожидаем 2 (1984, Fahrenheit 451)

# Выводим первую книгу (индексация работает только для физических книг!)
print(library[0])  # Ожидаем "1984"

# Выводим библиотеку в виде строки
print(str(library))  # Ожидаем "1984, Fahrenheit 451"

# Выводим библиотеку в виде представления (__repr__)
print(repr(library))  
# Ожидаем:
# Обычные книги: 1984, Fahrenheit 451!
# Электронные книги: Brave New World, Digital Fortress!