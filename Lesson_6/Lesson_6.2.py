

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def square_ms(self):
        return self._length * self._width

    def mass_of_road(self, square_weight, thinkness):
        asfalt_mass = self.square_ms() * square_weight * thinkness
        return asfalt_mass


my_road = Road(20, 10000)
print('Необходимая масса асфальта', my_road.mass_of_road(25, 5) // 1000, 'тонн')