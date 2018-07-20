__author__ = 'Cумароков Евгений Владимирович'
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

items = ["яблоко", "банан", "киви", "арбуз"]
i = 1
for item in items:
    print('{}. {:>6}'.format(i, item))
    i+=1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_1 = input('введите 1 список через запятую - ')
list_1 = list_1.split(',')
list_2 = input('введите 2 список через запятую - ')
list_2 =list_2.split(',')
new_list = [element for element in list_1 if not element in list_2 ]
print(new_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list_1 = [1,2,3,4,5,6,7,8,9]
new_list = [ element/4 if element//2 == 0 else element*2 for element in list_1 ]
print(new_list)