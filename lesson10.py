# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet_me(self):
#         greeting = f'Hello! My name is {self.name}! i am {self.age} years old'
#         print(greeting)
#
#
# person = Person('John', 25)
# person.greet_me()
#
# person2 = Person('Alice', 22)
# person2.greet_me()

# class Vehicle:
#     def __init__(self, speed, max_speed):
#         self.speed = speed
#         self.max_speed = max_speed
#
#     def accelerate(self, x):
#         self.speed += x
#         if self.speed > self.max_speed:
#             self.speed = self.max_speed
#
#     def brake(self, x):
#         self.speed -= x
#         if self.speed < 0:
#             self.speed = 0
#
#     def print_status(self):
#         print(f'Скорость транспортного средства равна {self.speed} км/ч')
#
# class Motorcycle(Vehicle):
#     def __init__(self, speed, max_speed):
#         Vehicle.__init__(self, speed, max_speed)
#         self._front_tire_width = 95
#         self._rear_tire_width = 95
#
#     def set_tires_width(self, front, rear):
#         self._rear_tire_width = rear
#         self._front_tire_width = front
#         print('На мотоцикл была установлена новые шины')
#         print(f'Скорость мотоцикла равна {self.speed} км/ч')
#
#     def tire_info(self):
#         print(f'Размер передней шины {self._front_tire_width}')
#         print(f'размер задней шины {self._rear_tire_width}')
#
# class Automobile(Vehicle):
#     def __init__(self, speed, max_speed):
#         Vehicle.__init__(self, speed, max_speed)
#         self._gear = 0
#         self._color = 'Silver'
#
#     def set_gear(self, gear):
#         self._gear = gear
#
#     def set_color(self, color):
#         self._color = color
#
#     def print_status(self):
#         Vehicle.print_status(self)
#         print(f'Автомобиль переключен на скорость №{self._gear}')
#         print(f'Автомобиль перекрашен в {self._color} цвет')
#
#     def get_color(self):
#         return self._color
#
# m = Motorcycle(40, 120)
# m.print_status()
# m.set_tires_width(100, 100)
# m.tire_info()
#
# a = Automobile(0, 150)
# a.accelerate(40)
# a.set_gear(2)
# a.print_status()
# a.set_color('Green')
# color = a.get_color()
# print(color)
#
# s = a.speed
# ms = a.max_speed
# print(s, ms)














