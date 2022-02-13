# 1

# dict_pers = {'name': input("Имя: "), 'surname': input("Фамилия: "), 'town': input("Город проживания: ")}
#
# with open('data.txt', 'w') as f:
#     file = f.writelines([el + '\n' for el in dict_pers.values()])


# def writer(dict_data):
#     with open("data.txt", 'w') as f:
#         file = f.writelines()
#
#     }
# while True:
#     for key, val in dict_pers.items():
#         if len(val) != 0:
#             # with open("data.txt", "w") as f:
#             #     file = f.writelines()
#             break
#         else:
#             print(f"Поле '{key}' не заполнено. Повторите попытку./n")
#             print()

# def o
# perations(oper, x, y):
#     return {
#         'add': lambda: x + y,
#         'sub': lambda: x - y,
#     }.get(oper, 'Not valid')
# print()
# print(type(operations('sub', 10, 5)))

# temp = eval('lambda x, y: x + y')
# print(temp(5, 6))

# 2


# with open("No_prog_text_5_2.txt") as f:
#     file = f.readlines()
# print(f"Количество строк в файле: {len(file)}.")
# for i, line in enumerate(file):
#     print(f"В {i+1}-й строке количество слов: {len(line.split(' '))}.")

# 3

# with open("No_prog_text_5_3.txt") as f:
#     file = f.readlines()
# lst_wages = []
# for line in file:
#     lst_param = line.split(" ")
#     lst_wages.append(float(lst_param[1]))
#     if float(lst_param[1]) < 20000.00:
#         print(f"{lst_param[0]} получает менее 20 000 рублей.")
# average_wage = sum(lst_wages)/len(lst_wages)
# print(f"Средняя зарплата сотрудника: {average_wage} рублей.")


# 4

# with open ("No_prog_text_5_4.txt") as f:
#     file = f.readlines()
# lst_rus_nums = ["Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять", "Десять"]
# lst_digit = [line.split(" - ")[1] for line in file]
# res = list(map(lambda x: " - ".join(x), list(zip(lst_rus_nums, lst_digit))))
# with open ("Prog_text_5_4.txt", "w") as f:
#     file = f.writelines(res)

# 5

# with open("Prog_text_5_5.txt", "w+") as f:
#     for i in range(100):
#         f.write(f"{i+1} ")
#     f.seek(0)
#     file = f.read()
# lst_nums = sum([int(item) for item in file.strip().split(" ")])
# print(lst_nums)

# 6


# import re

# with open("No_prog_text_5_6.txt") as f:
#     file = f.readlines()
# search_digit = [sum(list(map(int, item))) for item in [re.findall(r"\d+", line) for line in file]]
# search_subject = [re.findall(r"^\w+", line)[0] for line in file]
# res_dict = dict(zip(search_subject, search_digit))
# print(res_dict)


# 7


# import json

# with open('Prog_json_5_7.json', 'w') as f_w:
#     with open('No_prog_text_5_7.txt') as f_r:
#         profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_r}
#         result_lst = [profit, {'average_profit': sum([int(val) for val in profit.values() if int(val) > 0])}]
#     json.dump(result_lst, f_w)
