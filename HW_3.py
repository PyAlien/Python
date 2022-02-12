# 1
# num1 = input("Введите целое чиcло (делимое): ")
# num2 = input("Введите целое число (делитель): ")
#
#
# def div(num_1, num_2):
#     try:
#         num_1, num_2 = map(int, (num_1, num_2))
#         division = round(num_1 / num_2, 2)
#         return division
#     except ZeroDivisionError:
#         return "Ошибка. Деление на ноль!"
#     except ValueError:
#         return "Введите целое число!"
#     except TypeError:
#         return "Ошибка. Неверный тип данных!"
#
#
# print(div(num1, num2))


# 2
# dict_pers = {'name': input("Имя: "), 'surname': input("Фамилия: "), 'year_of_birth': input("Год рождения: "),
#              'town': input("Город проживания: "), 'email': input("E-mail: "), 'tel': input("Телефон: ")}
# for key, val in dict_pers.items():
#     if len(val) == 0:
#         print(f"Поле '{key}' не заполенено. Повторите попытку.")
#         break
#
# def person(**data_of_person):
#     return f"Данные пользователя: фамилия - {data_of_person['surname']}, " \
#            f"имя - {data_of_person['name']}, " \
#            f"год рождения - {dict_pers['year_of_birth']}, " \
#            f"город проживания - {dict_pers['town']}, " \
#            f"адрес электронной почты - '{dict_pers['email']}', " \
#            f"телефон - '{dict_pers['tel']}'"
#
# print(**dict_pers)


# 3
# def my_func(*tpl):
#     lst = list(tpl)
#     del lst[lst.index(min(lst))]
#     return sum(lst)
#
# try:
#     nums = tuple(map(int, (input("Введите число: "), input("Введите число: "), input("Введите число: "))))
#     print(my_func(*nums))
# except ValueError:
#     print("Ошибка! Введите числа.")


# 4
# 4.1
# a = float((input("Введите число: ")))
# b = int((input("Введите число: ")))
#
# def my_func(x, y):
#     exp = x ** y
#     return round(exp, 2)
#
# print(my_func(a, b))

# 4.2
# a = float((input("Введите число: ")))
# b = int((input("Введите число: ")))
#
# def my_func(x, y):
#     i = 1
#     base = x
#     while i < y:
#         i = i + 1
#         x = x * base
#     return round(x, 2)
#
# print(my_func(a, b))


# 5
# print('''Программа принимает строку из целых чисел разделенных пробелом.
# Выводит сумму, введенных чисел.
# Для завершения работы введите символ "#".''')
# stop = True
# lst = []
# while stop:
#     for el in input("Введите числа через пробел: ").split(' '):
#         if not el.isdigit() and el != '#':
#             print("Ошибка! Вы ввели неверный символ!")
#             stop = False
#         elif el == '#':
#             print("Завершение работы")
#             stop = False
#         else:
#             lst.append(int(el))
#     print(f"Сумма всех чисел: {sum(lst)}")
#     lst.append(sum(lst))
#     lst = lst[-1:]


# 6
# def int_func(text):
#     for word in text.split(" "):
#         i = 0
#         for el in word:
#             if ord(el) > 96 and ord(el) < 123:
#                 i += 1
#         if i == len(word):
#             print(word.title())
#         else:
#             print(f"Слово {word} должно быть в нижнем регистре")
#
# txt = input("Введите текст в нижнем регистре: ")
# int_func(txt)



# 7
# def int_func(text):
#     lst = text.split(" ")
#     y = 0
#     while y < len(lst):
#         word = lst.pop(y)
#         i = 0
#         for el in word:
#             if ord(el) > 96 and ord(el) < 123:
#                 i += 1
#         if i == len(word):
#            lst.insert(y, word.title())
#         else:
#             print(f"Слово {word} должно быть в нижнем регистре")
#         y += 1
#     return " ".join(lst)
#
# txt = input("Введите текст в нижнем регистре: ")
# print(int_func(txt))