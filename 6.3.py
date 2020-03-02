'''3. Реализовать базовый класс Worker (работник),
 в котором определить атрибуты: name, surname, position (должность)
 , income (доход). Последний атрибут должен быть защищенным
 и ссылаться на словарь, содержащий элементы: оклад и премия,
 например, {"wage": wage, "bonus": bonus}.
 Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного имени
 сотрудника (get_full_name) и дохода с учетом премии
 (get_total_income).

 Проверить работу примера на реальных данных
 (создать экземпляры класса Position, передать данные, проверить
 значения атрибутов, вызвать методы экземпляров).'''

class Worker:

    def __init__(self, name, surname, position, __income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = __income['wage']
        self._income_bonus = __income['bonus']

class Position(Worker):
    def get_full_name(self):
        self.full_name = self.name + self.surname + ', ' + self.position
        print(f'Полное имя сотрудника: {self.full_name}')

    def get_total_income(self):
        self.total_income = self._income_wage + self._income_bonus
        print(f'Доход с учётом премии: {self.total_income} руб.')

__my_dict = {"wage": 200000, "bonus": 75000}
my_obj = Position('Иван ', 'Иванов', 'ТОП-менеджер', __my_dict)
my_obj.get_full_name()
my_obj.get_total_income()


