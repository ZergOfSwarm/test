import os
#import sys
#import re

full_list = []
selected_list = []

def main():
    directory = "/home/denis/2/" # Откуда удалять.
    all_elements = os.listdir( directory ) # Список всех элиментов в папке.
    full_list = all_elements
    print(full_list,end='\n\n')

    for i in full_list:
        #selected_list.append(i[23:33] + i[35:43]) # Вытаскиваем дату и время в новый список! 
        selected_list.append(i[23:27] + i[28:30] + i[31:33] + i[35:37] + i[38:40] + i[41:43])
    print ('Отсортированный список - {}'.format(selected_list))


if (__name__ == "__main__"):
    main();
