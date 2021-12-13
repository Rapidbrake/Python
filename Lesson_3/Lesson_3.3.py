""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов. """

def my_func():
    try:
        a = int(input('Введите первое натуральное число:  '))
        b = int(input('Введите второе натуральное число:  '))
        c = int(input('Введите третье натуральное число:  '))
    except ValueError:
        return
    max_sum = 0
    if a and b > c:
        max_sum = a + b
    elif b and c > a:
        max_sum = c + b
    elif a and c > b:
        max_sum = a + c
    
    return max_sum

result = my_func()
print(result)



