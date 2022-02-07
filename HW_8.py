"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
данных. """

# class Date():
#     def __init__(self, date: str):
#         self.date = date
#     @classmethod
#     def get_int_fields(cls, date: str):
#         day, month, year = map(int, date.split("-"))
#         return day, month, year
#     @staticmethod
#     def validation(date: tuple):
#         if 1 <= date[0] <= 31 and 1 <= date[1] <= 12 and 1950 <= date[2] <= 2099:
#             print("Дата введена верно")
#         else:
#             print("Ошибка при вводе даты")
#
# user_input = input("Введите дату в формате 'число-месяц-год': ")
# date1 = Date(user_input)
# date1.validation(date1.get_int_fields(date1.date))


'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, 
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не 
завершиться с ошибкой. '''

# class Custom_Error(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# a, b = map(int, input("Введите делимое и делитель через пробел: ").split())
# try:
#     if b == 0:
#         raise Custom_Error("На ноль делить нельзя")
#     dev = a / b
#     print(f"Результат деления: {dev}")
# except Custom_Error as cust:
#     print(cust)

'''3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо 
только числами. Класс-исключение должен контролировать типы данных элементов списка. 
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу 
скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на 
экран. Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода 
пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если 
введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее 
сообщение. При этом работа скрипта не должна завершаться. '''

# class Custom_Error(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# lst_nums = []
# while True:
#     try:
#         user_input = input("Введите число: ")
#         if user_input == 'stop':
#             break
#         elif user_input.isdigit():
#             lst_nums.append(user_input)
#         else:
#             raise Custom_Error("Вы ввели строку")
#     except Custom_Error as cust:
#         print(cust)
#
# print(lst_nums)

'''4,5,6 Вместо предложенного проекта создан родительский класс игрового персонажа. Дочерние классы создают
три типа персонажей (Маги, Лучники, Рыцари). В классах реализованы атрибуты определяют базовые характеристики
персонажа, а также характеристики для каждого типа. Также реализованы методы, определяющие контроль 
и восстановление жизни персонажа, его передвижение, получение урона. Для каждого типа персонажей 
его дополнительная характеристика восполняется с помощью определенного метода. Оружие и магия выбирается
в соответствии с типом и имеет несколько вариантов.'''

# class Unit:
#     '''Базовый персонаж'''
#     def __init__(self, name, clan):
#         self.name = name
#         self.clan = clan
#         self.health = 100
#         self._speed = 5
#         self.__power = 10
#         self.__agility = 10
#         self.__intellect = 10
#     def get_status(self):
#         if 0 < self.health < 100:
#             return f"{self.clan} {self.name} need healing."
#         elif self.health == 100:
#             return f"{self.clan} {self.name} ready to fight!"
#         return f"{self.clan} {self.name} is dead. Brave guys always leave first."
#
#     def healing(self):
#         if self.health < 100:
#             self.health += 10
#
#     def go(self):
#         print(f"Moving at speed of {self._speed} kmph")
#
#     def take_damage(self):
#         if self.health > 10:
#             self.health -= 10
#             return f"{self.clan} {self.name} got hit."
#         self.health = 0
#         return f"{self.clan} {self.name} is dead. Brave guys always leave first."
#
#     def __str__(self):
#         return f"{self.name} {self.clan}"
#
#
# class Mage(Unit):
#     '''Маг'''
#     def __init__(self, name, clan, magic=None):
#         super().__init__(name, clan)
#         self.magic = {
#                 "air": "air",
#                 "fire": "fire",
#                 "water": "water"
#         }.get(magic, "hands")
#
#
#     def go(self):
#         return f"Moving at speed of {self._speed + 50} kmph"
#
#     def strengthen(self):
#         if self.__intellect < 10:
#             self.__intellect += 1
#
#
# class Archer(Unit):
#     '''Лучник'''
#     def __init__(self, name, clan,  weapon=None):
#         super().__init__(name, clan)
#         self.weapon = {
#             "bow": "bow",
#             "crossbow": "crossbow",
#         }.get(weapon, "hands")
#
#     def go(self):
#         return f"Moving at speed of {self._speed + 2} kmph"
#
#     def strengthen(self):
#         if self.__agility < 10:
#             self.__agility += 1
#
#
# class Knight(Unit):
#     '''Рыцарь'''
#     def __init__(self, name, clan, weapon=None):
#         super().__init__(name, clan)
#         self.weapon = {
#             "sword": "sword",
#             "axe": "axe",
#             "pike": "pike"
#         }.get(weapon, "Hands")
#
#     def go(self):
#         return f"Moving at speed of {self._speed - 2} kmph"
#
#     def strengthen(self):
#         if self.__power < 10:
#             self.__power += 1
#
# unit_1 = Mage("Zalman", "Legend", magic="air")
# unit_2 = Archer("Billy", "Mount", weapon="bow")
# unit_3 = Knight("Hofun", "Brave", weapon="axe")
# print(f"{unit_3.get_status()} My weapon is {unit_3.weapon}!")


'''7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (
комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного 
результата.'''

class Complex():
    def __init__(self, real, imag):
        self.r = real
        self.i = imag
    def get_complex(self):
        self.cmpl = f"({self.r}+{self.i}j)"
        return self.cmpl
    def __mul__(self, other):
        r_mul = self.r * other.r - self.i * other.i
        i_mul = self.i * other.r + self.r * other.i
        return Complex(r_mul, i_mul)
    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)
    def __sub__(self, other):
        return Complex(self.r - other.r, self.i - other.i)
    def __str__(self):
        if self.i > 0:
            return f"Результат операции:{self.r} + {self.i}j"
        return f"Результат операции: {self.r}{self.i}j"
# (a1a2 - b1b2) + (a1b1 + a2b1)j
c1 = Complex(2, 4)
c2 = Complex(3, 5)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)