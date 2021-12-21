""" 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т """

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def square_ms(self):
        return self._length * self._width

    def mass_of_road(self, square_weight, thinkness):
        asfalt_mass = self.square_ms() * square_weight * thinkness
        return asfalt_mass


my_road = Road(20, 5000)
print(f'Необходимая масса асфальта для полотна дороги площадью {my_road.square_ms()} квадратных метров,\nсотавляет {my_road.mass_of_road(25, 5) // 1000} тонн.')