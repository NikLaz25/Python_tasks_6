'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
 выведите результат. Выполните вызов методов и также покажите результат.'''

''' В данной задаче я добавил пару методов в базовый класс, 

чтобы задействовать все аргументы. Иначе зачем они были нужны?. 
Также созданы экземпляры классов для всех случаев.
В целом, формулировка задания на мой взгляд, крайне непонятна. Изначально было неясно, 
какой результат должна выводить программа. Разобрался только когда посмотрел, что выдает
 уже решенный пример. Но пока разбирался, успел руку набить. Может в этом и была задумка.
'''

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} движется')

    def stop(self):
        print(f'{self.name} стоит на месте. Приехали :)')

    def turn(self, way):
        print(f'{self.name} повернула {way}')

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed}')

    def show_color(self):
        print(f'{self.name} окрашена в {self.color} цвет')

    def find_cop(self):
        if self.is_police == False:
            print(f'Смотри {self.name} Спокуха. Это не менты :)')
        else:
            print(f'Смотри {self.name} Шухер, менты!!! :)')

class TownCar(Car):
    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed}')
        if self.speed > 60:
            print(f'{self.name} превышает скорость')
class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed}')
        if self.speed > 40:
            print(f'{self.name} превышает скорость')
class SportCar(Car):
    pass
class PolisetCar(Car):
    pass

my_obj1 = TownCar(70, 'Белый', 'Городска машина', False)
my_obj2 = WorkCar(100, 'серо-буро-малиновый', 'Рабочая машина', False)
my_obj3 = SportCar(270, 'Зелёный', 'Спортивная тачка', False)
my_obj4 = PolisetCar(150, 'крапинку', 'Ментовский УАЗик', True)

print('Скорость:')
my_obj1.show_speed()
my_obj2.show_speed()
my_obj3.show_speed()
my_obj4.show_speed()

print('\n', 'Цвет:')
my_obj1.show_color()
my_obj2.show_color()
my_obj3.show_color()
my_obj4.show_color()

print('\n', 'Повороты:')
my_obj1.turn('налево')
my_obj2.turn('направо')
my_obj3.turn('налево')
my_obj4.turn('направо')


print('\n', 'Движение:')
my_obj1.go()
my_obj2.go()
my_obj3.stop()
my_obj4.stop()

print('\n', 'Стоим на шухере:')
my_obj1.find_cop()
my_obj2.find_cop()
my_obj3.find_cop()
my_obj4.find_cop()
