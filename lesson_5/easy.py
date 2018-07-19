__author__ = 'Сумароков Евгений Владимирович'
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, fnmatch,shutil, sys

def do_dir():
    path = 'Dir_'
    for i in range(1,10):
        os.mkdir(path + str(i))
    n = 0
    while n !=1:
        n = int(input('если дирректории появились, напишите 1, чтобы их удалить - '))
        for i in range(1,10):
            os.rmdir(path + str(i))
    
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def all_folders():
    pattern = '.py'
    for folder in os.listdir():
        if os.path.isdir(folder):
          print('{}'.format( folder))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def do_copy():
    shutil.copy(sys.argv[0],os.getcwd()+'\\'+os.path.basename(sys.argv[0]).split('.')[0]+'(copy).py')
