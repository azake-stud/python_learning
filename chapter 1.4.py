# >>> (Вопрос 1) Выведите числа от 0 до 10 используя цикл while
# i = 0
# while i < 11:
#   print(i)
#   i += 1
#
# >>> (Вопрос 2) Выведите все нечетные числа от 0 до 20 использую while
# i = 0
# while i < 20:
#   i += 1
#   if (i % 2) == 0:
#     continue
#   else:
#     print(i)
#
# >>> (Вопрос 3) Вопрос не очень хорошо понял. Но стараюсь
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bilet = 0
# while True:
#     bilet = int(input('>>> Ведите и Угадайте число от 1 до 10 >>>  '))
#     if bilet in num_list:
#         print('*** Поздравляем! Вы угадали число ***')
#         break
#     else:
#         print('Попробуйте еще раз')
#
# >>> (Вопрос 4) Вопрос насчет паролья с трех попыток
# parol = 'simsim'
# popytka = 1
# while popytka != 4:
#     user = input('Введите пароль: ')
#     if user == parol:
#         print(f'*** Вы угадали пароль с {popytka} -раза ***')
#         break
#     else:
#         popytka += 1
#         if popytka < 4:
#             print('Попробуте еще раз ')
#         else:
#             print('Увы вы несмогли угадать пароль с 3 попыток <<<')
#
# >>> (Вопрос 5) Найти сколько чисел делятся на 'd' между двумя числами
# n1 = int(input('N1 : '))
# n2 = int(input('N2 : '))
# d = int(input('на сколько делить их? : '))
# new_list = []
# new_list2 = []
# cc = 0
# if n1 > n2:
#     mejdu_numbers = (n1 - n2 - 1)
#     print('**************************')
#     print(f'Между {n2} и {n1} ноходится {mejdu_numbers} чисел ')
#     for i in range(mejdu_numbers):
#         cc = (n2 + i + 1)
#         new_list.append(cc)
#     print(f'они >> {new_list}')
# else:
#     mejdu_numbers = (n2 - n1 - 1)
#     print('**************************')
#     print(f'Между {n1} и {n2} ноходится {mejdu_numbers} чисел ')
#     for i in range(mejdu_numbers):
#         cc = (n2 - i - 1)
#         new_list.append(cc)
#     print(f'они >> {new_list}')
#
# for j in range(len(new_list)):
#     if (new_list[j] % d) == 0:
#         new_list2.append(new_list[j])
# print(f'Количество чисел которые делятся ровно на {d} равно {len(new_list2)}')
# print(f'они >> {new_list2}')
# print('**************************')
#
# >>> (Вопрос 6) Треугольник ***
# n = int(input('input a number: '))
# for i in range(n):
#     print('*' * (n - i))
#
# >>> (Вопрос 7) Создать список до команды 'exit'
# user = ''
# list1 = []
# cc = 0
# print(' !!! Чтобы остановить процесс вводите слово "exit" !!!')
# while user != 'exit':
#     user = input('Введите имя студента: ')
#     list1.append(user)
#     cc += 1
# list1.pop()
# print(list1)
#
# >>> (Вопрос 8)
# n = int(input('input your age: '))
# cc = 0
# if n % 2 == 0:
#     print('Все четные числа до вашего возраста: ')
#     while cc != n:
#         if cc % 2 == 0:
#             print(cc)
#         cc += 1
# else:
#     print('Все НЕчетные числа до вашего возраста: ')
#     while cc != n:
#         if cc % 2 == 1:
#             print(cc)
#         cc += 1
#
# >>> (Вопрос 9) Вопрос не полностью понял
# n = int(input('Введите натуральное число: '))
# n_max = 0
# step = 1
# cc = 1
# for i in range(n):
#     step = (2 ** i)
#     if step < n:
#         n_max = step
#         cc = i
# print(f'максимальный степень двойки, результат которой не превышает {n} это {cc}')
# print(f'2^ {cc} =', n_max)
# print(f'>>> следующий степень: 2^ {cc +1} =', 2**(cc + 1))
#
# >>> (Вопрос 10) Вопрос похожий на поле чудес
# slovo = list('python')
# while True:
#     bukva = input('Введите букву: ')
#     if bukva == 'q':
#         print('Спасибо за попытки')
#         break
#     for i in range(0, len(slovo)):
#         if bukva == slovo[i]:
#             print(f'такая буква есть, в адресе {i}')
#
#
# >>>>> 10/10 <<<<<<
