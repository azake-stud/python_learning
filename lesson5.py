# x = 0
# for i in range(20):
#     x += 1
#     print('Python', x)

import time
# numbers = []
# for number in range(20):
#     numbers.append(number)
#     print(number)
#     time.sleep(0.3)
#
# print(numbers)

# >>>>>>> range(начало, конец, шаг) <<<<<<<<<<

# text = 'i love Python'
# for i in text:
#     print(i.upper())
#

# for i in range(40):
#     if i % 2 == 0 and i % 5 ==0:
#         print(i)

# i = 0
# while i <= 10:
#     print('True')
#     i +=1
#

# i = 0
# while True:
#     i += 1
#     print(i)
#     if i == 10:
#         break

# total = 100
# i = 0
# while i <5:
#     n = int(input('input number: '))
#     total -= n
#     i +=1
# print('Осталось ', total)

# i = 0
# while i < 20:
#     print('тестовая строка: ')
#     i = i + 1
#     if i == 10:
#         print('continue')
#         continue  #возврашает до while
#     print('continue не сработало')
#     if i == 18:
#         print('break')
#         break

# def is_palindrome():
#     text = input('input text: ')
#     if text == text[::-1]:
#         print('Yes')
#     else:
#         print('No')
# is_palindrome()

# def hello():
#     print('Hello')
# hello()  #если не вызвать функцию то оно не сработает
#

# name = input('input your name: ')
# def hello(name):
#     print(f"Hello, {name}")  # f строка это форматирование строка
# hello(name)

# def add (x, y):
#     print(x + y)
#
# add(10,10)

# def add (x, y):
#      return(x + y)
#
# print(add(7,8))

# def my_func():
#     name = 'Aza'
#     print('принт из функции ', name)
# my_func()
# #print(name) # << он не имеет доступа к переменной name

# def my_func(x,y):
#     z = x ** y
#     print(z)
#     return z
#
# var = my_func(2,3)
# print(var)

# num = 222  # переменная глобальная
# def my_func():
#     num = 111  # переменная локальная хотя названии похожы
#     print(num)
#
# my_func()
# print(num)

# def add (a, b, c, d, e):
#     return a + b + c + d + e
# print(add(1, 2, 3, 4, 5))

# def add2(*args):
#      result = 0
#      obj = args
#      for i in obj:
#          result +=1
#      return result
# nums = (1, 2, 3, 4, 5, 6, 7)
# print(add2(nums))   #>>>>>> Не понятная тема аргументы

# def my_func(x, y, z=10):
#     return x + y + z
# print(my_func(2,4))
#
# var = 'hello'
# print(var, var, var, sep=' ')

# def myfunc(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key} is {value}")
#
# myfunc(a=1, b=2, c=3, d=3, e=10)

# import time
# def recursive_func():
#     print('У папы была собака, он ее любил')                        # это рекурсия
#     print('Она сьела кусок мяса, он ее убил')
#     print('В землю закопал и надпись написал')
#     time.sleep(0.2)
#     recursive_func()
#
# recursive_func()


































































