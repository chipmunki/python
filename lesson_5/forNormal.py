# 1. Перейти в папку
def nextFolder():
    name = input(('Введите название папки: '))
    try:
        os.chdir(name)
        print('Успешно перешел. Текущая директория %s' % os.getcwd())
    except:
        
        print('Невезможно перейти в папку. Папка с именем %s не существует' % name)
        
# 2. Просмотреть содержимое текущей папки
import os,shutil, sys
def allFiles():
    for el in os.listdir():
        print(el)
# 3. Удалить папку
def removeFolder():
    name = input('Введите название папки: ')
    try:
        shutil.rmtree(os.getcwd()+'\\'+name)
        print('Папка успешно удалена!')
    except:
        print("Невозможно удалить папку. Папка с именем %s не существует" % name)
# 4. Создать папку
def createFolder():
    name = input("Введите название папки: ")
    try:
        os.mkdir(name)
        print("Папка успешно создана! ")
    except:
        print("Невозможно создать папку. Такая папка уже существует(( ")
      
