# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import forNormal, os
print('Вы находитесь здесь: %s .'%os.getcwd())
print('Введите команду: ')
print('1. Перейти в папку')
print('2. Просмотреть содержимое текущей папки')
print('3. Удалить папку')
print('4. Создать папку')
print('5. Выход из программы')
while True:
    key = input()
    if key == '1':
       forNormal.nextFolder()
    if key == '2':
        forNormal.allFiles()
    if key == '3':
        forNormal.removeFolder()
    if key == '4':
        forNormal.createFolder()
    if key == '5':
        print('До свидания')
        break
exit