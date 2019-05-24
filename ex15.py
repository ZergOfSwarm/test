from sys import argv
f = open('ext15_sample.txt') #Определяем название файла, что бы в конце его закрыть!

script, filename = argv

txt = open(filename)

#print(f"Here's your file {filename}:")
print("Here's your file {}" .format(filename))
print(txt.read())

#Удали ниже занк "#" и тогда получишь повторный запрос!
#print("Type the filename again:")
#file_again = input("> ")

#txt_again = open(file_again)

#print(txt_again.read())
f.close() # Всегда нужно закрывать открытые ранее файлы!
print("Файл закрыт/File is closed: ", f.closed)
