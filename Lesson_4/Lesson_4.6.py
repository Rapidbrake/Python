""" 6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено. """

from itertools import count

start = int(input('Введите стартовое число для диапазона генератора: '))
end = int(input('Введите конечное число для диапазона генератора: '))
for el in count(start):
    if el >= end:
        break
    else:
        print(el)


from itertools import cycle

rounds = int(input('Введите количество повторов списка: '))
i = 1
my_list = ['A', 'B', 'C', 'D']
for el in cycle(my_list):
    if i > rounds*len(my_list):
        break
    print(el)
    i += 1
