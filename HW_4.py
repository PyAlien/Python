# This Python file uses the following encoding: utf-8
# from sys import argv
# from functools import reduce
# from itertools import cycle, count

# 1


# def calc_wage():
#     num_of_hours, salary, bonus = map(int, argv[1:])
#     wage = (num_of_hours * salary) + bonus
#     return num_of_hours, salary, bonus, wage


# if __name__ == '__main__':
#     print(f"Заработная плата сотрудника: {calc_wage()[3]}\n"
#           f"Выработка в часах: {calc_wage()[0]}\n"
#           f"Cтавка в час: {calc_wage()[1]}\n"
#           f"Премия: {calc_wage()[2]}")


# 2


# num_lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_lst = [num_lst[i+1] for i in range(0, len(num_lst)-1) if num_lst[i+1] > num_lst[i]]
# print(new_lst)


# 3


# print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])


# 4


# source_lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# uniq_lst = [elem for elem in source_lst if source_lst.count(elem) == 1]
# print(uniq_lst)


# 5


# multiplication = reduce(lambda x, y: x * y, [elem for elem in range(100, 1001) if elem % 2 == 0])
# print(multiplication)


# 6


# 6.1 Итератор, генерирующий целые числа, начиная с указанного.
# for i in count(3, 1):
#     print(i)
#     if i == 10:
#         break

# 6.2 Итератор, повторяющий элементы некоторого списка, определённого заранее.
# lst = list(range(10))
# for i, j in enumerate(cycle(lst)):
#     print(j, end=" ")
#     if i > 80:
#         break


# 7


# def fact(n):
#     for i in range(1, n + 1):
#         if i == 1:
#             f = 1
#         f = f * i
#         yield f


# while True:
#     try:
#         num = int(input("Факториал какого числа вычислить? Введите число: "))
#         break
#     except ValueError:
#         print("Убедитесь, что введено число и запустите программу повторно.")

# k = 1
# for el in fact(num):
#     print(f"{k}! = {el}")
#     k = k + 1
