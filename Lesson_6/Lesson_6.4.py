""" 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат. """

class Car:
   
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed} км/ч'


class TownCar(Car):
    
    def show_speed(self):
        print(f'Текущая скорость {self.name} составляет {self.speed} км/ч')

        if self.speed > 40:
            return f'Cкорость автомобиля {self.name} выше разрешенной'
        else:
            return f'Aвтомобиль {self.name} не нарушает скоростной режим'

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    
    def show_speed(self):
        print(f'Текущая скорость {self.name} составляет {self.speed} км/ч.')

        if self.speed > 60:
            return f'Cкорость автомобиля {self.name} выше разрешенной на 10 км/ч.'


class PoliceCar(Car):
    
    def police(self):
        if self.is_police:
            return f'{self.name} это полицейский автомобиль'
        else:
            return f'{self.name} это не полицейский автомобиль'


audi = SportCar(100, 'красный', 'Ауди', False)
oka = TownCar(30, 'белый', 'Ока', False)
lada = WorkCar(70, 'баклажан', 'Лада приора', True)
ford = PoliceCar(110, 'бело-синий',  'Шкода', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, автомобиль {audi.stop()}')
print(f'{lada.go()} со скоростью {lada.speed} км/ч. {lada.show_speed()}')
print(f'{lada.name} в цвете {lada.color}')
print(f'{audi.name} это полицейский автомобиль? {audi.is_police}')
print(f'{lada.name} это полицейский автомобиль? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())