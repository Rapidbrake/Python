""" 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

def salary():
    try:
        time = float(input('Укажите выработку в часах: '))
        salary = int(input('Ставка в час: '))
        bonus = int(input('Размер Премии: '))
        res = time * salary + bonus
        print('Заработная плата сотрудника: ', res)
    except ValueError:
        return print('Не валидные данные!')
salary()
