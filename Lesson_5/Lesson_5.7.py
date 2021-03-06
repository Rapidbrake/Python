""" Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
    название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1   ООО   10000   5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
    в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
    Если фирма получила убытки, также добавить ее в словарь 
    (со значением убытков).
    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, 
    {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий 
    файл.
    Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, 
    {"average_profit": 2000}]
    Подсказка: использовать менеджер контекста. """


import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('Lesson_5\lesson5_7.txt', encoding='utf-8') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average profit - {prof_aver:.2f}')
    else:
        print(f'Average profit is null. All companies are unprofitable!')
    pr = {'Average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Profit of each company - {profit}')
with open(r'D:\!GeekBrains\Python\Lesson_5\new.json', 'w', encoding='utf-8') as file:
    json.dump(profit, file)

