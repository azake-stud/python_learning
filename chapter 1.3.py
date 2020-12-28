# >>>(Вопрос 1) Вывести те цифры которые меньше 5
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in range(11):
#     if a[i] < 5:
#         print(a[i])
#
# >>>(Вопрос 2) Нужно вернуть список, который состоит из элементов,
#   общих для этих двух списков .
# a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(set(a_list + b_list))
#
# >>>(Вопрос 3) Напишите программу для слияния нескольких словарей в один.
# dict1 = {'name': 'Jo', 'sur': 'Fam'}
# dict2 = {'age': 30, 'status': 'single'}
# dict3 = {'country': 'Kyrgyzstan', 'religion': 'islam'}
# dict_total = {**dict1, **dict2, **dict3}
# print(dict_total)
#
# >>>(Вопрос 4) Вывод четные числа, и brake когда встречает число 237
# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
# ]
# for i in numbers:
#     if i % 2 == 0:
#         print(i)
#     elif i == 237:
#         print('break')
#         break
#
# >>>(Вопрос 5) Пример: 10 14 >> Вывод все числа между ними: 10, 11, 12, 13, 14
# n1 = int(input('input start n1: '))
# n2 = int(input('input finish n2: '))
# for i in range(n2 - n1 + 1):
#     print(n1 + i)

# >>>(Вопрос 6)
# n1 = int(input('input start n1: '))
# n2 = int(input('input finish n2: '))
# for i in range(n2):
#     if ((i ** 2) < n2) and ((i ** 2) > n1):
#         print(i ** 2)
#
# >>>(Вопрос 7)
# num_list = [1, 2, 6, 3, 9, 2, 11, 20, 16, 7, 8]
# odd_num = 0
# even_num = 0
# for i in num_list:
#     if i % 2 == 0:
#         even_num += 1
#     else:
#         odd_num += 1
# print('общее кол-во чисел=', len(num_list))
# print('четные числа равно=', even_num)
# print('НЕчетные числа равно=', odd_num)
#
# >>>(Вопрос 8)
# for i in range(10):
#     print(str(i) * i)
#
# >>>(Вопрос 9) Создать таблицу умножения
# a = int(input('input a number: '))
# for i in range(10):
#     print(a, '*', (i + 1), '=', a * (i + 1))
#
# >>>(Вопрос 10)
# n1 = int(input('input a start number: '))
# n2 = int(input('input a finish number: '))
# sh = int(input('введите ШАГ: '))
# print(n1)
# for i in range(n1, n2, sh):
#     if (i + sh) < n2:
#         print(i + sh)
#
# >>>(Вопрос 11) Вывести ряд чисел из Фибонатчи до n-ного ряда
# fin = int(input('input a finish number:'))
# n1 = 1
# n2 = 1
# n3 = n1 + n2
# fib_list = [1, 1]
# for i in range(fin):
#     n3 = n1 + n2
#     fib_list.append(n3)
#     n1 = n2
#     n2 = n3
# print(fib_list)
#
# >>>(Вопрос 12) Вывести факториал
# n = int(input('input a number:'))
# f = 1
# for i in range(n):
#     f = f * (i + 1)
# print(n, '! =', f)
#
# >>>>> 12/12 <<<<<