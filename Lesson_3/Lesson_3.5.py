""" 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу. """


sum = 0
try:
    while True:
        for i in map(int, input('Введите числа через пробел: ').split()):
            sum += i
            if i == 'S':
                break
        print(sum)
except ValueError:
    print(sum, 'Невалидные данные')

