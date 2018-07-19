# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    lst = []
    a = 1
    b = 1
    for i in range(n-1):
        c = a+b
        a = b
        b = c
    lst.append(a)
    lst.append(b)
    for i in range(2,m-n+1,1):
        lst.append(lst[i-1]+lst[i-2])     
    return lst
n = int(input('Введите значение  n = '))
m = int(input('Введите значение  m = '))
print(fibonacci(n,m))
# 1 2 3 4 5 6 7 8 9 10
# 1 1 2 3 5 8 
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
def sort_to_max(origin_list):
	for i in range(len(origin_list)):
		j = i - 1 
		key = origin_list[i]
		while origin_list[j] > key and j >= 0:
			origin_list[j + 1] = origin_list[j]
			j -= 1
		origin_list[j + 1] = key
	return origin_list
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(function, lst):
    res = []
    for i in range(len(lst)):
        if function(lst[i]) == 1:
            res.append(lst[i])
    return res
def function(x):
    if x > 0:
        return 1
    else:
        return 0
x = [-1, 0, 2, -3, 4, 5, -2, 1]
print ('Non-filtered list', x)
print ('Filtered list', my_filter(function, x))
    

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
x1 = int(input('введите координату х1 = '))
y1 = int(input('введите координату y1 = '))
x2 = int(input('введите координату х2 = '))
y2 = int(input('введите координату y2 = '))
x3 = int(input('введите координату х3 = '))
y3 = int(input('введите координату y3 = '))
x4 = int(input('введите координату х4 = '))
y4 = int(input('введите координату y4 = '))
if (y3+y1)/2==(y2+y4)/2 and (x3+x1)/2==(x2+x4)/2:
     print('точки являются вершинами параллелограма))')
else:
     print('точки не являются вершинами параллелограма((')
