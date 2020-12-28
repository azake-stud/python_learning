# class MyClass:
#     pass
#
# class User:
#     def __init__(self, name):
#         self.name = name
#         print(f'Появился новый пользователь с именем {self.name}')
#
# firs_user = User('Erkin')
# second_user = User('Ratmir')
#
# class Pet:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#         print('Poyavilsya noviy obekt')
#
#     def __str__(self):
#         text = f"Объект класса Pet с именем {self.name}, это у нас {self.type}"
#         return text
#
#     def talk(self, sound):
#         print(sound)
#
# bobik = Pet('Bobik', 'dog')
# bobik.talk('gav gav')
# barsik = Pet('Barsik', 'Cat')
# barsik.talk('Miyao')
# print(barsik)
# bobik.type = 'Cat'
# print(bobik)

# class A:      #инкапсуляция
#     def _private(self):                   #метод находится внутри класса
#         print('Это закрытый метод')
#
# a = A()
# a._private()
#
# class B:
#     def __private(self):
#         print('Это защищенный метод', self.__private())
# b = B()
# b.__private()
# print(b)

# class Dog:
#     def __init__(self, name):
#         self.name = name
#         print('Сработал конструктор в классе Dog')
#
# class Doberman(Dog):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Сработал конструктор в классе Doberman')
#     def talk(self, sound='Gav'):
#         print(sound)
#
# dog1 = Doberman('Dogggg', 2)
# dog1.talk()

class Table:

    def __init__(self, l=1, w=2, h=1):
        self.length = l
        self.width = w
        self.height = h
        print('Вы создали объект, поэтому видите эту строку. Сработад метод __init__')


class KitchenTable(Table):

    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p


class DeskTable(Table):

    def square(self):
        return self.width * self.length


t1 = KitchenTable(1, 1, 1.5, 2)
t2 = DeskTable(1.5, 0.8, 0.75)
t3 = KitchenTable(1, 1.2, 0.8, 2)
t4 = Table(1, 1, 0.5)
print(t2.square)


class CompTable(DeskTable):

    def square(self, e):
        #return self.width * self.length - e
        return DeskTable.square(self) - e


ct = CompTable(2, 1, 1)
print(ct.square(0.3))




















