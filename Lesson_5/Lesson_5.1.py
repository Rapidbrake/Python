""" 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка. """

my_file = open('Lesson_5\lesson5_1.txt', 'w', encoding='utf-8')
line = input('Введите текст: \n')
while line:
    my_file.writelines(line + '\n')
    line = input('Введите текст: \n')
    if not line:
        break
my_file.close()

my_file = open('Lesson_5\lesson5_1.txt', 'r', encoding='utf-8')
content = my_file.readlines()
print(content)
my_file.close()