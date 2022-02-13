# 1
# class Matrix:
#     def __init__(self, mtrx):
#         self.mtrx = mtrx
#
#     def __str__(self):
#         return '\n'.join([''.join([f'{i}\t' for i in row]) for row in self.mtrx])
#
#     def __add__(self, other):
#         return Matrix(list(map(lambda x, y: list(map(lambda w, z: w + z, x, y)), self.mtrx, other.mtrx)))
#
#
# matrix1 = [[1, 2, 3], [5, 6, 7], [8, 9, 10]]
# matrix2 = [[1, 2, 3], [5, 6, 7], [8, 9, 10]]
# m1 = Matrix(matrix1)
# m2 = Matrix(matrix2)
# print(m1 + m2)


# 2
# from abc import ABC, abstractmethod
#
# class Clothes(ABC):
#     items = []
#
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#         self._required_fabric_size = None
#         self.items.append(self)
#     @property
#     @abstractmethod
#     def _fabric_consumption(self):
#         """Метод расчета требуемой ткани"""
#         raise NotImplemented
#
#     @property
#     def required_fabric_size(self):
#         """Если размер ткани известен заранее, то расчет не производим"""
#         if not self._required_fabric_size:
#             self._fabric_consumption()
#
#         return self._required_fabric_size
#
#     @classmethod
#     def total_consumption(cls):
#         """Суммарный расчет затраченной ткани на все изделия"""
#         return f"Для всех изделий потребуется \
# {round(sum([item.required_fabric_size for item in cls.items])/100, 2)} кв.м ткани"
#
#
# class Suit(Clothes):
#
#     def _fabric_consumption(self):
#         self._required_fabric_size = 2 * self.size + 0.3
#
#     @property
#     def H(self):
#         return self.size
#
#     def __str__(self):
#         return f"На костюм {self.name} потребуется {round(self.required_fabric_size/100, 2)} кв.м ткани"
#
#
# class Coat(Clothes):
#
#     def _fabric_consumption(self):
#         self._required_fabric_size = self.size / 6.5 + 0.5
#
#     @property
#     def V(self):
#         return self.size
#
#     def __str__(self):
#         return f"На пальто {self.name} потребуется {round(self.required_fabric_size/100, 2)} кв.м ткани"
#
#
# s = Suit('для Виктора', 175)
# print(s)
# print(s.H)
# print(s.required_fabric_size)
# c = Coat('для Кристины', 42)
# print(c)
# print(c.V)
# print(c.required_fabric_size)
# print(Clothes.total_consumption())


# 3
# class Cell:
#     def __init__(self, count):
#         self.count = int(count)
#
#     def __add__(self, other):
#         return f'Объединение двух клеток. Количество ячеек : {self.count + other.count}'
#
#     def __sub__(self, other):
#         sub = self.count - other.count
#         return f'Уменьшение клетки. Количество ячеек: {sub}' if sub > 0 else 'Клетка погибла'
#
#     def __mul__(self, other):
#         return f'Умножение клеток. Количество ячеек: {self.count * other.count}'
#
#     def __truediv__(self, other):
#         div = self.count // other.count
#         return f'Деление клеток. Количество ячеек: {div}' if div > 0 else 'Клетка погибла'
#
#     def make_order(self, line):
#         structure = ''
#         for el in range(int(self.count / line)):
#             structure += '*' * line + '\n'
#         structure += '*' * (self.count % line) + '\n'
#         return structure
#
#
# cell1 = Cell(15)
# cell2 = Cell(25)
# print(cell1 + cell2)
# print(cell1 - cell2)
# print(cell1 * cell2)
# print(cell1 / cell2)
# print(cell2.make_order(3))
