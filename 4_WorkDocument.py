# Базовый класс Shape, который задает имя фигуры
class Shape:
    def __init__(self, name):
        self.name = name  # Устанавливаем имя фигуры

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"  # Вывод информации об объекте

# Класс Rectangle наследуется от Shape (Прямоугольник — это тоже фигура)
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")  # Вызываем конструктор родителя, передавая "Rectangle"
        self.width = width  # Устанавливаем ширину
        self.height = height  # Устанавливаем высоту

    def __repr__(self):
        return f"{self.__class__.__name__} (width = {self.width}, height = {self.height})"
        # Вывод информации о прямоугольнике (его ширина и высота)

    def area(self):
        return self.width * self.height  # Метод для вычисления площади (ширина * высота)

    def __len__(self):
        return 2 * (self.width * self.height)  # Ошибка! Это не периметр, а удвоенная площадь

    def __call__(self, width, height):
        self.width = width  # Изменяем ширину объекта
        self.height = height  # Изменяем высоту объекта

# Создаем прямоугольник с шириной 5 и высотой 10
rect = Rectangle(5, 10)

# Выводим информацию о прямоугольнике
print(rect)

# Вычисляем и выводим площадь
print("Area - ", rect.area())

# Вычисляем и выводим "периметр", но здесь ошибка, так как используется удвоенная площадь
print("Perimetr - ", len(rect))

# Меняем размеры прямоугольника с помощью вызова объекта как функции
rect(7, 12)

# Выводим обновленный прямоугольник
print(rect)

# Вычисляем и выводим новую площадь
print("Area - ", rect.area())

# Вычисляем и снова выводим "перим