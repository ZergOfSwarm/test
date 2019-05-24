import re
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "") # Для отображения даты в той локали которая по дефолту! 
now = datetime.now()
splited_word = []
new_sw = []
new_a = []

a = ['design_code_data_files_2019-05-17__14-20-06.tgz', 'design_code_data_files_2019-05-18__14-22-06.tgz', 'design_code_data_files_2019-05-16__10-20-06.tgz']

x = 'design_code_data_files_2019-05-18__14-22-06.tgz'
print ('Из такого вида.')
print(x, end='\n\n')

def splited_word():
    result = list(x)
    splited_word = result
    return result
splited_word = splited_word()

def new_sw():
    new_sw = splited_word[3+4]


for i in [a]: # Перебираем каждый элимент в списке "а"
    if x in i: # Проверяем списк на наличе элемента "x"
        print('Привел к такому виду, где каждый элимент по отдельности!')
        print (splited_word, end='\n\n')
        splited_word[23 : 43] = [''.join(splited_word[23 : 43])] # Объеденяем нужные элименты!
        print (splited_word, end='\n\n')
        data = now.strftime("%Y-%m-%d")
        time = now.strftime("%H-%M-%S")
        print('Просто вывод даты м времени.')
        print (data, time, end='\n\n')

        #----------Регулярное вырожение --------------

        pattern = re.compile(r'\d')
        matches = pattern.finditer(x)
        #print(match) # выдаст <_sre.SRE_Match object; span=(38, 39), match='2'>
        print('Вытаскиваем нужную инфу из нашего выбранного элимента!')
        print('Дата - {}'.format(x[23:33]))
        print('Время - {}'.format(x[35:43]),end='\n\n')

    else:
        print ('no')

print('Удаляем все из нашего элимента, кроме цифр!')
for i in [x]:
    splited_word = re.sub("\D","", str(splited_word)) # Приводим к такому виду 20190517142006
    new_x = splited_word
    print('и прмводим к такому виду {}'.format(new_x))
    splited_number = list(new_x) # Делим наше число на отдельные элименты
    splited_number[0 : 8] = [''.join(splited_number[0 : 8])] # Объеденяем сначала дату!
    joined_data = splited_number
    joined_data[1 : 7]= [''.join(joined_data[1 : 7])] # Объеденяем теперь время!
    print('Создаем список в котором только дата и время -{} '.format(joined_data))





