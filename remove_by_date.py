import os
from datetime import datetime

N = 3 # Количество бакапов в которые оставляем.
full_list = []
selected_list = []
sorted_list = []
a = 'design_code_data_files_'
b = '.tgz'

def main():
    directory = "/home/denis/test/2/" # Откуда удалять.
    all_elements = os.listdir( directory ) # Список всех элиментов в папке.
    full_list = all_elements
    print('Список всех элиментов.')
    print(full_list,end='\n\n')


    for i in full_list:
        #selected_list.append(i[23:27] + i[28:30] + i[31:33] + i[35:37] + i[38:40] + i[41:43])
        selected_list.append(i[23:43])
    print ('Выделили только дату и время из имен файлов!')
    print(selected_list,end='\n\n')
    print ('Выбранные элименты сортируем по дате!')
    selected_list.sort(key=lambda date: datetime.strptime(date,"%Y-%m-%d__%H-%M-%S"))
    print(selected_list,end='\n\n')


    files_to_live = selected_list[-N:] # Делаем срез, что бы выделить нужные бакапы!
    print ('Список файлов  которые будут оствлены -{}'.format(files_to_live),end='\n\n')
    files_to_delete = selected_list[:-N] # Делаем срез, что бы вылелить список удаляемых файлов!
    print()
    print('Список файлов который удаляем!-{}'.format(files_to_delete),end='\n\n')

    for i in files_to_delete: # Перебираем весь список.
        del_file = directory + a+i+b
        print('Удалили -{}'.format(del_file)) # Выписываем все элименты которые бедут удалены.
        os.remove(del_file) # Удалем!


if (__name__ == "__main__"):
    main();
