import os
from datetime import datetime

full_list = []
selected_list = []
sorted_list = []
N = 3 # Количество первых бакапов в списке которые оставляем!

def main():
    directory = "/home/denis/test/2" # Откуда удалять.
    all_elements = os.listdir( directory ) # Список всех элиментов в папке.
    full_list = all_elements
    print('Список всех элиментов.')
    print(full_list,end='\n\n')

    for i in full_list:
        selected_list.append(i[23:27] + i[28:30] + i[31:33] + i[35:37] + i[38:40] + i[41:43])
    print ('Выделили только дату и время из имен файлов!')
    print(selected_list,end='\n\n')
    print ('Выбранные элименты сортируем по дате!')
    selected_list.sort(key=lambda date: datetime.strptime(date, "%Y%m%d%H%M%S"))
    print(selected_list,end='\n\n')
    sorted_list = selected_list
    sorted_list = sorted(selected_list, reverse = True) # Делаем обратную сортировку!
    print ('Список в ктором последняя дата на первом месте!')
    print(sorted_list,end='\n\n')
    files_to_delete = sorted_list[N:] # Делаем срез, что бы оставить нужное количество файлов!
    print ('Список который будет удален -{}'.format(files_to_delete))
    files_to_live = sorted_list[:N] # Делаем срез, что бы удалить оставшиеся количество файлов!
    print('Список который останется!')
    print(files_to_live,end='\n\n')


    for file in files_to_delete: # Перебираем весь список.
        #i = directory + file  # путь + имя файла
        #if os.path.isfile(i):
            #os.remove(i) # Удалем!
        print('Удалили -{}'.format(file)) # Выписываем все элименты которые бедут удалены.
        os.remove(file) # Удалем!




if (__name__ == "__main__"):
    main();
