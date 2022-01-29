"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата 
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать 
число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить 
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных 
данных. """

class Date():
    def __init__(self, date):
        self.date = date
    @classmethod
    def set_cls_field(cls, date):
        cls.day, cls.month, cls.year = map(int, date.split("-"))
        print(cls.day, cls.month, cls.year)
    @staticmethod
    def validate(day, month, year):


date1 = Date("21-02-2022")
date1.set_cls_field("21-02-2001")

date2 = Date("21-02-2022")
print(date1.date)