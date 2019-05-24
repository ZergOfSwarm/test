import random
words_list = ['Cheese', 'Window', 'Dog']

def function_to_chooce_word():
    chooced_word = random.choice(words_list)
    return chooced_word

def splited_word():
    resalt = list(function_to_chooce_word())
    return resalt

def number_items_in_the_list():
    resalt = len(splited_word()) # подсчет элиментов в списке!
    return resalt


print(function_to_chooce_word())
print(splited_word())
print(number_items_in_the_list())

#print(counting_items_in_the_list())
a = list(('?',)*number_items_in_the_list())

print(a)
