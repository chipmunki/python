__author__ = 'Cумароков Евгений Владимирович'
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print('exersice 1')
from math import sqrt
list_1 = [2, -5, 8, 9, -25, 25, 4]
list_2 = [int(sqrt(element)) for element in list_1 if (element>0 and sqrt(element)- int(sqrt(element))==0)]
print(list_2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print('exersice 2')
n = input('Vvedite datu:  dd.mm.yyyy = ')
day = {"01":"first","02":"second","03":"third","04":"fourth","05":"fifth","06":"sixth","07":"seventh","08":"eighth","09":"nineth","10":"tenth","11":"eleventh","12":"twelfth","13":"thirteenth","14":"fourteenth","15":"fifteenth","16":"sixteenth","17":"seventeenth","18":"eighteenth","19":"nineteenth","20":"twentieth","21":"twenty-first","22":"twenty-second","23":"twenty-third","24":"twenty-fourth","25":"twenty-fifth","26":"twenty-sixth","27":"twenty-seventh","28":"twenty-eighth","29":"twenty-nineth","30":"thirtieth","31":"thirty-first"}
month = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
print(day[n[:2]],month[n[3:5]],n[-4:],'year')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print('exersice 3')
import random
n = int(input('vvedite n = '))
lst_1 = [random.randint(-100,100) for enement in range(n)]
print(lst_1)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print('exersice 4')
lst = [1, 2, 4, 5, 6, 2, 5, 2]
#a
list_1 = list(set(lst))
print('lst2 = ',list_1)
#б
list_3 = [element for element in lst if  lst.count(element)==1]
print('lst2 = ',list_3)
