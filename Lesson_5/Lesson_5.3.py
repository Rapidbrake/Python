""" 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников. """


with open('Lesson_5\lesson5_3.txt', 'r', encoding='utf-8') as my_file:
    sal = []
    penniless = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        print(i)
        if int(i[1]) < 20000:
           penniless.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {penniless}, средний оклад {sum(map(int, sal)) / len(sal)}')