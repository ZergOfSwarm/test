import os
#import sys
import re
#import shutil

selected_list = []
full_list = []
delete_list = []

def main():
    #print('Hello, Denis! Below is a list according to your search criteria! \n------------------\n')
    directory = "/home/denis/test/2/" # Откуда удалять.
    all_elements = os.listdir( directory ) # Список всех элиментов в папке.
    full_list = all_elements
    selection_criteria = re.compile("design_code_data_files*.*")  # Сортируем список согласно критерию «Regular expressions»
    selected_files = list(filter(selection_criteria.match, full_list)) #
    selected_list = selected_files

    #result=list(set(selected_list) & set(full_list)) # Создаст список совпадений.
    #result=list(set(selected_list + full_list)) # Создаст список из уникальных элиментов.
    result=list(set(selected_list) ^ set(full_list)) # Создаст список элиментов которые не соответствуют критерию сортировки. 
    delete_list = result # Список элиментов на удаление.

    print("List of all elements in selected folder - {}".format(all_elements), end='\n\n')
    #print("List which will delete: - {}".format(delete_list),end='\n\n')
    #print("." * 10)
    #print("list which will stay: - {}".format(selected_list))




    for file in delete_list: # Перебираеи весь список.
        i = directory + file  # путь + имя файла
        if os.path.isfile(i): # Проверяем является ли элимент файлом.
            #os.remove(i) # Удалем!
            print('Удалили -{}'.format(i)) # Выписываем все элименты       которые бедут удалены.



if (__name__ == "__main__"):
    main();
