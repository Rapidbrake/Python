""" 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. """


def summary():
    try:
        with open(r'D:\!GeekBrains\Python\Lesson_5\lesson5_5.txt', 'w+', encoding='utf-8') as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода!')
summary()