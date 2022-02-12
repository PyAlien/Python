"""1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе. """

# lst = ['Bob', 40, 2.5, None, False, -5]
#
# def func_type(lst):
#     for el in lst:
#         print(type(el))
#
# func_type(lst)

"""2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 
2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов 
нужно использовать функцию input(). """

# el_count = int(input("Введите количество элементов списка: "))
# lst = []
# i = 0
#
# while i < el_count:
#     lst.append(input("Введите значение элемента списка: "))
#     i += 1
#
# if len(lst) % 2 != 0:
#     temp = lst.pop()
#     for j in range(0, len(lst), 2):
#         lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     lst.append(temp)
# else:
#     for j in range(0, len(lst), 2):
#         lst[j], lst[j + 1] = lst[j + 1], lst[j]
#
# print(lst)

"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (
зима, весна, лето, осень). Напишите решения через list и dict. """

# lst_seasons = ['winter', 'spring', 'summer', 'autumn']
# dct_seasons = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
# month = int(input("Введите месяц по номеру: "))
#
# for key, val in dct_seasons.items():
#     if month in val:
#         print(key)
#     else:
#         print(f"Это не {key}")
#
# if month in (12, 1, 2):
#     print(lst_seasons[0])
# elif month in (3, 4, 5):
#     print(lst_seasons[1])
# elif month in (6, 7, 8):
#     print(lst_seasons[2])
# elif month in (9, 10, 11):
#     print(lst_seasons[3])
# else:
#     print("Такого месяца не существует")

"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. 
Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове. """

# words = input("введите слова через пробел: ").split(" ")
# i = 1
# for word in words:
#     if len(word) > 10:
#         print(f"{i} {word[:10]} {len(word)}")
#         i += 1
#     else:
#         print(f"{i} {word} {len(word)}")
#         i += 1

"""5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У 
пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них. """

# num = int(input("Введите натуральное число: "))
# lst = [10, 9, 7, 7, 5, 3, 3, 1]
#
# pos = 0
# for el in lst:
#     if num <= el:
#         pos += 1
#
# lst.insert(pos, num)
# print(lst)

"""6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит 
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, 
то есть характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать 
программно, запросив все данные у пользователя. """

# final = []
# params_item = {"name": "", "price": "", "count": "", "measure_unit": ""}
# num_item = 0
# while True:
#     if input("To exit, enter 'exit' or press 'Enter': ").lower() == "exit":
#         break
#     num_item += 1
#     params_item = params_item.copy()
#     for param in params_item.keys():
#         while True:
#             try:
#                 data = input(f"{param}: ")
#                 params_item[param] = int(data) if param in ("price", "count") else data
#                 break
#             except ValueError:
#                 print('Неверный формат')
#     item = num_item, params_item
#     final.append(item)
# print(final)
