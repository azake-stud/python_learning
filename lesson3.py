#dictionary -словарь  то есть в листе содержится переменная и значение вместе
# new_dict = {}
# new_dict2 = dict()
#
# print('1', type(new_dict))
# print('2', type(new_dict2))
# print('3', dir(new_dict))

# new_dict = {'key': 'value', 'key': 'value2', 'Erkin': '0755099065'}
# print(new_dict)

# capitals = {} # means it is a dict or >>> capitals = dict()
# capitals['Kyrg'] = 'Bish'
# capitals['Rus'] = 'Moscow'
# print(capitals)

# capitals = dict(Russia='Moscow', Kyrg='Bish', USA='Wash')
# print(capitals)

# capitals = dict([('Russia','Moscow'), ('Kyrg', 'Bish'), ('USA', 'Wash')])
# print(capitals)
#
# new_dict = dict(zip([('Russia','Kyrg','USA'), (, 'Bish'), (, 'Wash')]))  dumai******

# method fromkeys создает словарь из ключей
# capitals = dict(Russia='Moscow', Kyrg='Bish', USA='Wash')
#dictionary = dict.fromkeys(['key1', 'key2'], 'какое-то значение')
# print(dictionary)
# name = None

#method get получает значение по ключу
# print(dictionary.get('key1'))
# print(capitals.get('Russia'))

# method keys выводит все ключи из словаря
# method values выводит все значения
# method items возврашает пару ключ и значение
# method pop удаляет по ключу и возврашает нам значенте

# capitals = dict(Russia='Moscow', Kyrg='Bish', USA='Wash')
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
#
# russia = capitals.pop('Russia')
# print(russia)
# print(capitals)

# method update

# capitals = dict(Russia='Moscow', Kyrg='Bish', USA='Wash')
# capitals2 = {'Belarus': 'Minsk', 'Russia': 'Kiev'}
# capitals.update(capitals2)
# print(capitals)
#
# new_dict = capitals | capitals2 #тоже самое но работает в версиях Python 3.9
# print(new_dict)

# method popitem не принимает аргументы, удаляет последний элемент
# capitals = dict(Russia='Moscow', Kyrg='Bish', USA='Wash')
# usa = capitals.popitem()
# print(capitals)
# kg = capitals.popitem()
# print(usa)    #ask ???
# print(capitals)

# method setdefault
# capitals = dict(Russia='Moscow', Kyrg='Bish', USA='Wash')
# new = capitals.setdefault('China')
# print(new)
# print(capitals)
