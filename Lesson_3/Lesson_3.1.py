""" 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль. """

def my_div():
    print('Программа предназначена для вычисления результата деления. Числа должны быть натуральными!')
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
    except Exception:
        return

    if a < 0 or b <= 0:
        return

    return a/b 

result = my_div()
if result:
    print(f'Результат деления равен {result}')
else:
    print('Введены невалидные данные! Проверьте, числа должны быть натуральными')



      

