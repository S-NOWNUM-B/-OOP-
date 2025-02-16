from abc import ABC, abstractmethod

class Payable(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payable):
    def __init__(self, balance, limit):
        self.__balance = balance
        self.__limit = limit

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    def pay(self, amount):
        if self.__balance + self.__limit >= amount:
            self.__balance -= amount
            print(f"Оплачено {amount}. Новый баланс: {self.__balance}")
        else:
            print("Недостаточно средств (включая кредитный лимит).")

class Person:
    def __init__(self, name, age, credit_card):
        self.__name = name
        self.__age = max(18, age)
        self.credit_card = credit_card

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 18:
            self.__age = value
        else:
            print("Возраст не может быть меньше 18 лет.")

    def introduce(self):
        return f"Меня зовут {self.__name}, мне {self.__age} лет."

class Student(Person, Payable):
    def __init__(self, name, age, university, credit_card):
        super().__init__(name, age, credit_card)
        self.university = university

    def pay(self, amount):
        discounted_amount = amount * 0.9  # 10% скидка
        self.credit_card.pay(discounted_amount)

class Employee(Person, Payable):
    def __init__(self, name, age, salary, credit_card):
        super().__init__(name, age, credit_card)
        self.salary = salary

    def pay(self, amount):
        self.credit_card.pay(amount)

# Тестирование
person = Person("Alice", 25, CreditCard(1000, 5000))
student = Student("Bob", 20, "MIT", CreditCard(1000, 3000))
employee = Employee("John", 35, 50000, CreditCard(2000, 10000))

print(student.introduce())
print(employee.introduce())

student.pay(200)
employee.pay(200)