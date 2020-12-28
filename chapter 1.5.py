# >>> (Вопрос 1) Проверка слово на палиндром
# soz = input('Введите слово: ')
# if soz == soz[::-1]:
#     print('True')
# else:
#     print('False')
#
# >>> (Вопрос 2)
# soz = input('input a word: ')
# bukva = input('input a bukva: ')
# cc = int(soz.count(bukva))
# print(f'в слове "{soz}" есть {cc} букв "{bukva}"')
# print(f'Первая из них под индексом {soz.index(bukva)}')
# print(f'Последняя из них под индексом {soz.rindex(bukva)}')
#
# >>> (Вопрос 3) Сумма случайных трех цифр
# import random
# n1 = random.randint(1, 50)
# n2 = random.randint(51, 100)
# n3 = random.randint(100, 150)
# print(n1, '+', n2, '+', n3, '=', (n1 + n2 + n3))
#
# >>> (Вопрос 4) Отсортировать слова по количеству слов
# slova = input('введите слова через пробел: ')
# newList = sorted(slova.split())
# print(newList)
#
# >>> (Вопрос 5) Вопрос чуть не понятный
# bukva = input('Введите букву: ')
# soz = 'Hello World!'
# if bukva in soz:
#     print('Hello')
# else:
#     print('Bye')
#
# >>> (Вопрос 6) Не понял слово "кратны". У меня тут те цифры которые делятся ровно на 7 и 5
# for i in range(1500, 2701):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)
#
# >>> (Вопрос 7) Вывести цифры от 0 до 6 кроме 3 и 6 исползуя continue
# for i in range(7):
#     if i == 3 or i == 6:
#         continue
#     else:
#         print(i)
#
# >>> (Вопрос 8)
# Честно скажу вопрос не понял(( по моему тут про функции идеть речь, но не уверень
#
# >>> (Вопрос 9) Посчитать количество букв и цифр в введенном строке
# slovo = list(input('Введите слово и цифры: '))
# nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# cc_b = 0 #счетчик буквы
# cc_c = 0 #счетчик цифры
# for i in range(len(slovo)):
#     if slovo[i] in nums:
#         cc_c += 1
#     else:
#         cc_b += 1
#     # print(i)
# print('количество букв: ', cc_b)
# print('количество цифр: ', cc_c)
#
# >>> (Вопрос 10) Проверка букв на гластность и не гластность
# glasnaya = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# bukva = input('Введите букву: ')
# if bukva in glasnaya:
#      print('Гласная')
# else:
#      print('Не гласная')
#
# >>> (Вопрос 11) Создать список пока не вводится слово 'end' и вывести sum all, average
# new_list = []
# cc = 0 #счетчик для общей суммы
# i = 0 #счетчик для цикла
# n = ''
# while n != 'end':
#     n = input('Введите цифру: ')
#     if n != 'end':
#         new_list.insert(i, int(n))
#         i += 1
#     else:
#         for j in range(len(new_list)):
#             cc += new_list[j]
#         print(new_list)
#         print('summa>>', cc)
#         print('average>>', cc / len(new_list))
#         break
#
# >>> (Вопрос 12)
# name1 = input('Введите имя: ')
# surname1 = input('Введите фамилию: ')
# year1 = int(input('Введите год рождения: '))
# country = input('Введите страну проживания: ')
# print(f'Здравствуйте {surname1} {name1}, вам {2020 - year1} лет и вы живете в {country}')
#
# >>> (Вопрос 13) Конкатенция
# yoda = ['on Python', 'programming', 'I like']
# yoda2 = yoda[-1] + ' ' + yoda[1] + ' ' + yoda[0]
# print(yoda)
# print(yoda2)
#
# >>> (Вопрос 14) Оценки учеников используя dic
# marks = {
#     'Bill': 0,
#     'Jane': 0,
#     'John': 0,
#     'Mary': 0
# }
# marks["Bill"] = int(input('Введите оценку для Bill: '))
# marks["Jane"] = int(input('Введите оценку для Jane: '))
# marks["John"] = int(input('Введите оценку для John: '))
# marks["Mary"] = int(input('Введите оценку для Mary: '))
# print(marks)
# print('Average mark is: ', (marks["Bill"] + marks["Jane"] + marks['John'] + marks['Mary']) / 4)
#
# >>> (Вопрос 15) тот же вопрос, как (Вопрос 11).
#
#
# >>>>> 15/15 <<<<<<
