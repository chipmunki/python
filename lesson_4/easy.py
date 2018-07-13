___authour__ = 'Сумароков Евгений Владимирович'
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
print('{:*^30}'.format(' exersice_1 ' ))
import random
lst = [random.randint(-10,10) for _ in range(4)]
lst1 =[element**2 for element in lst]
print('{} --> {}'.format(lst,lst1))


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print('{:*^30}'.format(' exersice_2 '))
list_1 = ['apple', 'peach', 'melon', 'pineapple', 'lemon', 'watermelon']
list_2 = ['melon','orange', 'lemon', 'lime', 'grape']
list_new = [element for element in list_1 if element in list_2]
print(list_new)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
print('{:*^30}'.format(' exersice_3 '))
list1 = [random.randint(-100,100) for _ in range(10)]
listnew = [element for element in list1 if element%3==0 or element>0 or element%4 != 0]
print(listnew)
#непонятно условие, если необходимо выполение всех 3-х условий то так:
print('{:*^30}'.format(' exersice_3.1 '))
list11 = [random.randint(-100,100) for _ in range(20)]
listnew1 = [element for element in list11 if (element%3==0 and element>0 and element%4!=0)]
print(listnew1)
