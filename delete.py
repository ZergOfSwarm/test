import os
from glob import glob

selected_list = []
full_list = []
delete_list = []

def main():
    #print('Hello, Denis! Below is a list according to your search criteria! \n------------------\n')
    directory = "/home/denis/test/"
    all_elements = glob("/home/denis/test/*.*") # Список всех элиментов в папке!
    full_list = all_elements
    selected_files = glob("/home/denis/test/Den*.*") # Сортируем список согласно критерию!
    selected_list = selected_files
    print("This is a selected list - {}".format(selected_list),end='\n\n')
    print("List of all elements in selected folder - {}".format(full_list),end='\n\n')
    #result=list(set(selected_list) & set(full_list)) # Создаст список совпадений
    #result=list(set(selected_list + full_list)) # Создаст список из уникальных элиментов.
    result=list(set(selected_list) ^ set(full_list)) # Создаст список элиментов которые соответсвуют критерию сортировки.
    delete_list = result
    print("List which will delete: -  {}".format(delete_list),end='\n\n')



# цикл не работает!

    for file in delete_list: # перебираем все элименты в списке
        if file in delete_list: # Если элимент есть в списке
            if os.path.isfile(file): # Если это файл 
                os.remove(file) # то удаляем его!
if (__name__ == "__main__"):
    main();
