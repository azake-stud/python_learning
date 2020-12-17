# set
# new_set = {9, 2, 3, 4, 5, 6, 1, 8 } #automatic упорядочиваеть
# print(new_set)
#
# new_set = set{}
# print(type(set_)) #look
#
# method add  #добавляеть только один элемент, апдейт добавляеть множество элементов
# method update() принимает один оргумент -iterable, и добавляет его элементы к исходному элементу

# a_set = {1, 2, 0, ('sad', 'all')}
# a_set.add(4)
# print(a_set)
#
# a_set.add('4')
# print(a_set)

# list_ = [2, 3, 4, 6, 8, 0, 9]
# b_set = {5, 6, 7, 8}
# a_set.update(list_)
# print(a_set)
#
# a_set = {1, 2, 0, ('sad', 'all')}
# # method remove
# a_set.remove(1)   # >>> look
# print(a_set)

# method discard

# a_set.discard(2)
# a_set.remove(0)
# print(a_set)

# method pop, method clear()
# a_set = {1, 2, 0, 6, ('sad', 'all')}
# # print(a_set.pop())
# a_set.clear()
# print(a_set)

# method union() возвращает новое множество, содержашее
# все элементы каждого из множеств
# a_set = {2, 4, 5, 9, 12, 30, 51, 76, 127, 195}
# b_set = {1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}
# a_set.union(b_set)
# print(a_set)

# method intersection() возвращает новое множество, которое есть во обоих групп данных
# set1 = {1, 2, 3, 4, 5}
# set2 = {0, 2, 4, 7}
# # set3 = set1.intersection(set2)
# # print(set3)
#
# # method difference() возвращает все элементы от сет1 которые нету у  сета2
# print(set1.difference(set2))  #разность только со одной стороны
#
# # method symmetric_difference возвращает новое множество,
# # которое содержит только уникальные элементы обоих множеств
#
# print(set1.symmetric_difference(set2)) #разность с обоих сторон

# method Boolean
# x = 1
# y = 2
#
# if x < 0:
#     print(True)
# elif y < 0:
#     print(True)
# else:
#     print('сработал блок else')

####################################################################################
# == Сравнение
# != Отрицание
# < меньше
# <= меньшн равно
# > больше
# >= больше равно
# and и
# or или
# not не

# point = input('Enter your point: ') # он по умолчанию принимает как string
# if point == '5'
#     print('Молодец')
# elif point == '4'
#     print('Молодец, чуть прибавь ходу')
# elif point == '3'
#     print('Старайся учиться лучше')
# else:
#     print('Ты можешь лучше учиться')

# list_ = [1, 2, 3, 4, 5]
# num = int(input('enter a number: '))
# if num in list_:
#     print('есть такое число')
# else:
#     print('Введите число ')

### обратная условия
# if num not in list_:
#     print('такого числа нет ')
# else:
#     print('есть такое число ')


# Calculator
# while True:
#     number1 = int(input('enter a number1: '))
#     number2 = int(input('enter a number2: '))
#     oper = input('enter an operator +, -, *, /')
#
#     if oper == '+':
#         print(number1 + number2)
#     elif oper == '-':
#         print(number1 - number2)
#     elif oper == '*':
#         print(number1 * number2)
#     elif oper == '/':
#         print(number1 / number2)
#     elif oper == 'stop':
#         break
#
#     else:
#         print('Введите только +,-,*,/')
#
#
