# Базовый класс Collection, который работает с коллекциями элементов (в данном случае - книг)
class Collection:
    def __init__(self, items):
        if not isinstance(items, list):  # Проверяем, что переданный items — это список
            raise ValueError("items must be a list")  # Если нет, выбрасываем ошибку
        self.items = items  # Сохраняем список элементов

    def __repr__(self):
        return f"Collection(items = {self.items})"  # Строковое представление объекта

    def __len__(self):
        return len(self.items)  # Позволяет использовать len() для подсчёта элементов

    def __getitem__(self, item):
        return self.items[item]  # Доступ к элементам коллекции через []

    def __call__(self):
        return ",".join(str(item) for item in self.items)  # Вызывает объект как функцию и возвращает элементы через запятую

# Класс BookCollection расширяет Collection, добавляя жанр книг
class BookCollection(Collection):
    def __init__(self, items, ganre):  # Ошибка! "ganre" → "genre"
        super().__init__(items)  # Вызываем конструктор родительского класса
        self.ganre = ganre  # Добавляем жанр

    def __repr__(self):
        return f"BookCollection(items = {self.items}, ganre = {self.ganre})"
        # Улучшенный вывод: отображает книги и их жанр

    def __add__(self, other):
        if not isinstance(other, BookCollection):  # Проверяем, что складываем две коллекции книг
            raise TypeError("Can only combine with another BookCollection")  # Ошибка, если тип не совпадает
        if self.ganre != other.ganre:  # Если жанры разные, нельзя объединять
            return "Cannot combine collections with different ganre"  # Ошибка (и еще опечатка в "ganre")
        return BookCollection(self.items + other.items, self.ganre)  # Объединяем две коллекции книг

# Создаем первую коллекцию книг с жанром "Fiction"
collection1 = BookCollection(["Book1", "Book2", "Book3"], "Fiction")

# Создаем вторую коллекцию книг с таким же жанром
collection2 = BookCollection(["Book4", "Book5", "Book6"], "Fiction")

# Создаем третью коллекцию книг, но с другим жанром
collection3 = BookCollection(["Book7", "Book8"], "Non-Fiction")

# Пытаемся объединить три коллекции
combined = collection1 + collection2 + collection3  # Ошибка! Нельзя объединить Fiction и Non-Fiction

# Выводим результат объединения (ожидаем ошибку, так как жанры разные)
print(combined)