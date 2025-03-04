#Задание 1
#
# import time
# import functools
# from abc import ABC, abstractmethod
#
# def log_execution(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"[LOG] Начало выполнения: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# def track_time(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         print(f"[LOG] Время выполнения {func.__name__}: {end_time - start_time: .6f} секунд")
#         return result
#     return wrapper
#
# class Storage(ABC):
#     @abstractmethod
#     def save(self, filename: str, date: str):
#         pass
#
# class LocalStorage(Storage):
#     @log_execution
#     @track_time
#     def save(self, filename: str, date: str):
#         time.sleep(0.5)
#         with open(filename, "w") as file:
#             file.write(date)
#             print(f"[LocalStorage] Файл '{filename}' загружен в облако")
#
# class CloudStorage(Storage):
#     @log_execution
#     @track_time
#     def save(self, filename: str, data: str):
#         time.sleep(1)
#         print(f"[CloudStorage] Файл '{filename}' загружен в облако")
#
# local = LocalStorage()
# cloud = CloudStorage()
#
# local.save("local_file.txt", "Hello, Local")
# cloud.save("cloud_file.txt", "Hello, Cloud")

# Задание 2
#
# from abc import ABC, abstractmethod
# import functools
#
# user_role = "admin"
#
# def permission_required(role):
#     def class_decorator(cls):
#         origin_make_sound = cls.make_sound
#
#         @functools.wraps(origin_make_sound)
#         def wrapped_make_sound(self, *args, **kwargs):
#             if user_role != role:
#                 raise PermissionError(f"Доступ запрещён для роли '{user_role}'. Требуеться роль '{role}'")
#             return origin_make_sound(self, *args, **kwargs)
#
#         cls.make_sound = wrapped_make_sound
#         return cls
#     return class_decorator
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         print("Собака говорит: Гав-гав!")
#
# class Cat(Animal):
#     def make_sound(self):
#         print("Кошка говоритЖ Мяу-мяу!")
#
# @permission_required("admin")
# class Lion(Animal):
#     def make_sound(self):
#         print("Лев рычит: Рррррр!")
#
# if __name__ == '__main__':
#     dog = Dog()
#     cat = Cat()
#     lion = Lion()
#
#     dog.make_sound()
#     cat.make_sound()
#
#     try:
#         lion.make_sound()
#     except PermissionError as e:
#         print(f"Ошибка доступа: {e}")

#Задание 3
#
# from abc import ABC, abstractmethod
# import functools
#
# def log_class_methods():
#     def class_decorator(cls):
#         for attr_name in dir(cls):
#             attr = getattr(cls, attr_name)
#             if callable(attr) and not attr_name.startswith("__"):
#                 @functools.wraps(attr)
#                 def logged_method(method):
#                     @functools.wraps(method)
#                     def wrapper(*args, **kwargs):
#                         print(f"Метод {method.__name__} вызван")
#                         return method(*args, **kwargs)
#                     return wrapper
#                 setattr(cls, attr_name, logged_method(attr))
#         return cls
#     return class_decorator
#
# class Vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
# @log_class_methods()
# class Car(Vehicle):
#     def move(self):
#         print("Автомобиль едет по дороге.")
#
# @log_class_methods()
# class Bicycle(Vehicle):
#     def move(self):
#         print("Велосипед движется по велосипедной дорожке.")
#
# @log_class_methods()
# class Airplane(Vehicle):
#     def move(self):
#         print("Самолет летит в небе.")
#
# if __name__ == "__main__":
#     car = Car()
#     bicycle = Bicycle()
#     airplane = Airplane()
#
#     car.move()
#     bicycle.move()
#     airplane.move()