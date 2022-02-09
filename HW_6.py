# 1

# from time import sleep
#
# class TrafficLight:
#     def __init__(self, color):
#         self.color = color
#     def running(self):
#         if self.color == "red":
#             print("Загорается красный сигнал светофора")
#             sleep(7)
#         elif self.color == "yellow":
#             print("Загорается желтый сигнал светофора")
#             sleep(2)
#         elif self.color == "green":
#             print("Загорается зеленый сигнал светофора")
#             sleep(5)
#
# a = TrafficLight("red")
# a.running()

# 2

# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#     def calc_of_mass(self, mass_piece, asphalt_thickness):
#         self.mass_piece = mass_piece
#         self.asphalt_thickness = asphalt_thickness
#         return self._length * self._width * self.mass_piece * self.asphalt_thickness
#
# f = Road(length=20, width=5000)
# print(f"Масса асфальта: {f.calc_of_mass(25, 5)} кг.")

# 3

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#        self.name = name
#        self.surname = surname
#        self.position = position
#        self._income = {"wage": wage, "bonus": bonus}
#
# class Position(Worker):
#     def get_full_name(self):
#         full_name = self.name + ' ' + self.surname
#         return full_name
#     def get_total_income(self):
#         income = self._income["wage"] + self._income["bonus"]
#         return income
#
# f = Position('Иван', 'Иванов', 'Менеджер', 50000, 12000)
# print(f"Полное имя сотрудника: {f.get_full_name()},\n"\
#       f"Доход сотрудника: {f.get_total_income()} рублей")
