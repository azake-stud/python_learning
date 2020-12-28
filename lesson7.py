# РАБОТА С ФАЙЛАМИ

# file = open('text.txt', 'w')
# file.write('hello ')
# file.close()

# with open('text.txt') as f:
#     text = f.read(3)      #ошончо char окуйт
#     print(text)


#with open('text.txt', 'a') as f:
     # print(f)
     # f.write('\npython')

# with open('new_file.txt', 'w') as file:
#     for i in range(50):
#         file.write('Good\n')

# with open('new_file.txt', 'r') as file:
#     for line_ in file:
#         line_ = file.readline()
#         print(line_.replace('\n', ''))

# try:
#     x = 100 / 0
#     print(x)
# except ZeroDivisionError:     #если не знаем код ошибкт то вводим except Exception as ex:
#     print('Ошибка деление на ноль')
#
# print('А код все рпано работает')
#
# def add_lines_to_file():
#     file = open('1.txt', 'w')
#     nums = [i for i in range(20)]
#     for i in nums:
#         file.write(str(i)+ '\n')
#
# file = open('1.txt', 'r')
# nums = []
#
# try:
#     for line in file:
#         nums.append(int(line))
# except ValueError:
#     print('Это не цифра')
# else:
#     print('Все хорошо')
# finally:
#     file.close()
#     print('Я закрыл файл')
# print(nums)

import random
# #
# a = [random.randint(1, 100) for i in range(100)]
# # a.sort()
# print('a:', a)
# print('sorted a: ', sorted(a))

# x = random.randint(1, 100)
# print(x)

# x = random.randrange(1,50,3)
# print(x)
#
# y = random.random()  # 0.0 - 1.0
# print(y)

# list_ = [
#     'Эржигит',
#     'Алтынай',
#     'Миргуль',
#     'Азамат Р',
#     'Анвар',
#     'Байэл',
#     'Ажар',
#     'Сыймык',
#     'Азамат А'
#     ]
# print(random.choice(list_))

# try:
#     list_ = [1, 2, 3, 4]
#     print(list_[3])
# except IndexError as error:
#     print(error)
# else:
#     print('Ошибки нет')
#















