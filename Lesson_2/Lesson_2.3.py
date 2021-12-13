""" 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
 Напишите решения через list и через dict. """



""" Через список """

try:                                                #Общая часть
    number = int(input('Введите номер месяца: '))   #Общая часть
except ValueError:                                  #Общая часть
        print('Так ведь нет такого месяца! ;)')     #Общая часть

else:
    season_1 = [1, 2, 12]
    season_2 = [3, 4, 5]
    season_3 = [6, 7, 8]
    season_4 = [9, 10, 11]
    if number in season_1:
        print('Зима')
    elif number in season_2:
        print('Весна')
    elif number in season_3:
        print('Лето')
    elif number in season_4:
        print('Осень')
    if number > 12:
        print('Так ведь нет такого месяца! ;)')
    if number < 1:
        print('Так ведь нет такого месяца! ;)')




""" Через словарь        """ 

""" season = {}
season = season.fromkeys([1, 2, 12], 'Зима')
season.update({}.fromkeys([3, 4, 5], 'Весна'))
season.update({}.fromkeys([6, 7, 8], 'Лето'))
season.update({}.fromkeys([9, 10, 11], 'Весна'))

print(season.get(number))
if number > 12:
    print('Так ведь нет такого месяца! ;)')
if number < 1:
    print('Так ведь нет такого месяца! ;)') """
