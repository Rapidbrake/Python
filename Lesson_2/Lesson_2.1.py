""" 1. Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе. """

my_list = [34, 56, 'Lesson', False, 55.4]
for type_el in my_list:
    print(type(type_el))
    