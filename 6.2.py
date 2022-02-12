'''2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), 
width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, 
необходимого для покрытия всего дорожного полотна. Использовать формулу: 
длина ширина масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т'''

class Road:
    def __init__(self, length, weigth):
        self.length = length
        self.weigth = weigth


    def my_func(self, thick):
        self.thick = thick
        mas = self.length * self.weigth * thick * 25 / 1000
        print(f'Масса {mas} тонн')

result_obj = Road(int(input('Задайте длину, м: ')), int(input('Задайте ширину, м: ')))
result_obj.my_func(int(input('Задайте толщину, см: ')))


# Ниже первоначальный вариант который я сделал без init
# class Road:
#
#     __length, __weigth = int(input('Задайте длину, м: ')), int(input('Задайте ширину, м: '))
#     def my_func(self, thick):
#         self.thick = thick
#         mas = self.__length * self.__weigth * thick * 25 / 1000
#         print(f'Масса {mas} тонн')
#
# result_obj = Road()
# result_obj.my_func(int(input('Задайте толщину, см: ')))
