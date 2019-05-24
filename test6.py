import random
words_list = ['Cheese', 'Window', 'Dog']

def function_to_chooce_word():
    chooced_word = random.choice(words_list)
    return chooced_word

function_to_chooce_word = function_to_chooce_word()

def splited_word():
    resalt = list(function_to_chooce_word)
    return resalt

splited_word = splited_word()

def number_items_in_the_list():
    resalt = len(splited_word) # подсчет элиментов в списке!
    return resalt

number_items_in_the_list = number_items_in_the_list()

#print(function_to_chooce_word())
#print(splited_word())
#print(number_items_in_the_list())
#print(counting_items_in_the_list())

print('This is the selected word - "{}"'.format(function_to_chooce_word))
print('This is the splited word - "{}"'.format(splited_word))
print('The number of items in our list it is - "{}"'.format(number_items_in_the_list))

a = list('?',)*number_items_in_the_list

print('The number of hidden items must = number of items in our list! - {}'.format(a))
#print(a)
