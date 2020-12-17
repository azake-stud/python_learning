# from datetime import datetime
#
# start = datetime.now()
# nums = [num for num in range(2000000)]
# ## print(nums)
# finish = datetime.now()
#
# start2 = datetime.now()
# num2 = []
# for i in range(2000000):
#     num2.append(i)
#     ###print(nums)
# finish2 = datetime.now()
# print(datetime.now())
# print(datetime.timestamp(datetime.now()))
# print(finish - start)
# print(finish2 - start2)




# Lambda
# my_func = lambda x, y: x + y
# print(my_func(10,10))
#
# def add(x,y):
#     return x + y
# print(add(10,10))

# list_ = [1, 2, 3, 4, 5, 6]
# def my_func(x):
#     return x**x
#
# new_list = list(map(my_func, list_))
# print(new_list)

# nums = [1, 2, 3, 4, 5]
# def my_func(x):
#     x+=10
#     return x
#
# nums2 = list(map(my_func, nums))
# print(nums2)

# text1 = 'i love you'
# def my_func(x):
#     return x.upper()
#
# text2 = list(map(my_func, text1))
# print(text2)
# text3 = ''.join(text2)
# print(text3)

# mixed = ['prosto', 'mak', 'mak', 'prosto', 'mak', 'mak']
# my_filter = lambda x: x == 'mak'
# zolushka = list(filter(my_filter, mixed))
# print(zolushka)

# from functools import reduce
# nums = [x for x in range(50)]
# lambda_func = lambda x, y: x + y
# def add(x, y):
#     return x+y
# summ_all = reduce(add, nums)
# print(summ_all)

# ZIP

# text1 = 'hello world'
# nums = [x for x in range(20)]
# tuple_ = ('a', 'b', 'c', 'd', 'e')
#
# zip_func = list(zip(text1, nums, tuple_))  # или tuples
# print(zip_func)  # он принимает из всех массивов по одной элемтов и соединяет их во одиг массив или спискор











