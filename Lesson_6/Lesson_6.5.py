

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    
    def draw(self):
        super().draw()
        return f'Мы взяли {self.title}. Мы рисуем ручкой'


class Pencil(Stationary):
    
    def draw(self):
        super().draw()
        return f'Мы взяли {self.title}. Мы рисуем карандашом'


class Handle(Stationary):
    
    def draw(self):
        super().draw()
        return f'Мы взяли {self.title}. Мы рисуем маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())