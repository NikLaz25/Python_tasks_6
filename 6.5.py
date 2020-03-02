'''5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(self.title,'Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print(self.title,'Запуск отрисовки для ручки')
class Pencil(Stationery):
    def draw(self):
        print(self.title,'Запуск отрисовки для карандаша')
class Handle(Stationery):
    def draw(self):
        print(self.title,'Запуск отрисовки для маркера')
my_obj1 = Stationery('Атрибут для Stationery. ')
my_obj1.draw()
my_obj2 = Pen('Атрибут для Pen.')
my_obj2.draw()
my_obj3 = Pencil('Атрибут для Pencil.')
my_obj3.draw()
my_obj4 = Handle('Атрибут для Handle.')
my_obj4.draw()

# Как ни странно, последняя задача оказалась лёгкой.
# Может быть по сравлнению с предыдущими задачами