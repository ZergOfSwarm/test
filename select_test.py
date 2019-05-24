#!/usr/bin/python3
import os
import sys
import re
#import shutil

selected_list = []
selected_list_2 = []
full_list = []
full_list_2 = []
delete_list = []
delete_list_2 = []
splited_word = []


def main():
    #print('Hello, Denis! Below is a list according to your search criteria! \n------------------\n')
    directory = "/home/denis/test/"
    all_elements = os.listdir( directory ) # Список всех элиментов в папке!
    full_list = all_elements
    selection_criteria = re.compile("design_code_data_files*.*")  # Сортируем список согласно критерию «Regular expressions»
    selected_files = list(filter(selection_criteria.match, full_list)) #
    selected_list = selected_files

    #result=list(set(selected_list) & set(full_list)) # Создаст список совпадений
    #result=list(set(selected_list + full_list)) # Создаст список из уникальных элиментов.
    result=list(set(selected_list) ^ set(full_list)) # Создаст список элиментов которые соответсвуют критерию сортировки. 
    delete_list = result

    #print("Список всех вайлов в выбранной папке - {}".format(all_elements), end='\n\n')
    print('Список всех файлов в выбранной папке.', end='\n')
    print(all_elements, end='\n\n')
    #print("Список элиментов которые будут удалены!: - {}".format(delete_list),end='\n\n')
    print('Список всех файлов которые будут удалены!', end='\n')
    print(delete_list, end='\n\n')
    #print("." * 10)
    #print("Список файлов которые стануться после удаления - {}".format(selected_list))
    print('Список файлов которые стануться после удаления.', end='\n')
    print(selected_list, end='\n\n')

    def splited_word():
        resalt = list(selected_list)
        return resalt
    splited_word = splited_word()
    print(splited_word)

    for file in delete_list: # Перебираеи весь список
        i = directory + file  # путь + имя файла
        if os.path.isfile(i): # Проверяем является ли элимент файлом
            os.remove(i) # Удалем!

# сортируе по дате
    all_elements_2 = os.listdir( directory ) # Список всех элиментов в папке!
    full_list_2 = all_elements_2


    text_to_search = 'design_code_data_files_2019-05-18__14-20-06.tgz'
    pattern = re.compile(r'2019-05-16__10-20-06')
    matches  = pattern.finditer(text_to_search)

    for match in matches:
        print(match)

    #print('Второй список всех файлов после первой селекции.', end='\n')
    #print(all_elements_2, end='\n\n')
    #print('Второй список всех файлов которые будут удалены!', end='\n')
    #print(delete_list_2, end='\n\n')
    #print('Второй список файлов которые стануться после удаления.', end='\n')
    #print(selected_list_2, end='\n\n')



if (__name__ == "__main__"):
    main();
