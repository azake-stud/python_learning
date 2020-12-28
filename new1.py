# new_list = []
# empty_list = list()
# list_ = [1, 2, 3, 4, 5, 6]
# print(list_)
# print(len(list_))
#
# diapazon = range(1, 21)
# print(list(range(1,21)))


# # method append добавляет элементы в список
# some_list = [1, 2, 3, 4, 5]
# print(some_list)
# some_list.append(6)
# print(some_list)
#
# some_list.append('python')
# print(some_list)
#
# print(len(some_list))
#
# new_list = [1, 2, 3]
# some_list.append(new_list)
# print(some_list)
# print(len(some_list))
# """


# list1 = ['user1', 'user2', 'user3']
# list2 = ['Erkin', 'Kirill', 'Aika']
# list1 = list1 + list2
# list1 += list2
# list1.extend(list2)
# print(list1)
# print(list2)

# method insert получает 2 аргумента и добавляет в список поиндексу

# cars = ['Mers', 'Honda', 'Subaru']
# print(cars)
# cars.insert(2, 'Toyota')
# print(cars)

# method remove удаляеть элементы по значению

# laptops = ['Lenovo', 'MacB', 'Acer', 'Asus', 'HP']
# laptops.remove('Asus')
# print(laptops)

# method pop метод удаляет по умолчанию последний элементб но можно передать индекс удаляемого элемента
#
# laptops = ['Lenovo', 'MacB', 'Acer', 'Asus', 'HP']
# notebook = laptops.pop(1)
# last_notebook = laptops.pop()
# print(laptops)
# print(notebook)
# print(last_notebook)

# method index возврашает индекс элемента
# laptops = ['Lenovo', 'MacB', 'Acer', 'Asus', 'HP']
# print(laptops.index('Asus'))

# method count
# numbers = [1, 2, 3, 4, 5, 6]
# print(numbers.count(2))

# method reverse разворочивает список
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.reverse()
# print(numbers)

# method sort сортирует по ключу
# nums = [5, 3, 7, 9, 2, 0, 4]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)

# laptops = ['Lenovo', 'MacB', 'Acer', 'Asus', 'HP']
# laptops.sort(key=len, reverse=True)
# print(laptops)

# method copy
# cars= ['Mers', 'Honda', 'Subaru', ['hello', 'world']]
# print(cars)
# new_cars = cars.copy()
# new_cars[3][0] = 'BMW'
# print(new_cars)

# method deepcopy
# import copy
# list_ = [1, 2, 3, [4, 5, 6]]
# print('Original', list_)
#
# new_list = copy.deepcopy(list_)
# print('Copy', new_list)
# new_list[3][0] = 'Changed'
#
# print('copy', new_list)
# print('original', list_)

# method clear
# cars= ['Mers', 'Honda', 'Subaru', ['hello', 'world']]
# # cars.clear()
# del cars[1]
# print(cars)

# from datetime import datetime
# print(datetime.now())

# срезы
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_[0:5])
# print(list_[1::2])  #списки изменяемые

# кортежи -tuples /они не изменяемые

# new_tuples = ('abc',)
# print(type(new_tuples))
# tuple_ = tuple()
# print(type(tuple_))

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0)
# print(numbers.index(3))
# print(numbers.count(0))
#
# numbers = list(numbers)
# print(numbers)
# numbers.clear()
# numbers











