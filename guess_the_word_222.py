import random

words_list = ['Chees', 'Milk', 'Window', 'Bird', 'Door']

hidden_list = ['?']

def Congratulations_1():
    print("Wow, CONGRATULATIONS!!!")
    print("You have guessed the word!!!")
    print("You are a WINNER!!!!!!!!!!!!!!")
#Congratulations_1 = Congratulations_1()

def Congratulations_2():
    print("WOW, tere is such the letter in our word!")
    return 
#Congratulations_2 = Congratulations_2()

def function_to_chooce_word():
    chooced_word = random.choice(words_list)
    return chooced_word
function_to_chooce_word = function_to_chooce_word()

def counting_items_in_the_list():
    resalt = len(function_to_chooce_word) # подсчет элиментов в списке!
    return resalt
counting_items_in_the_list = counting_items_in_the_list()

def splited_word():
    resalt = list(function_to_chooce_word)
    return resalt
splited_word = splited_word()

def counting_matches_in_newlist():
    resalt = splited_word.count(splited_word) # подсчет совпадений в списке!
    return resalt
counting_matches_in_newlist = counting_matches_in_newlist()

def new_hidden_list():
    new_hidden_list = list(hidden_list*counting_items_in_the_list)
    return new_hidden_list
new_hidden_list = new_hidden_list()

def gues_the_word():
    b = splited_word
    print('Hint for diagnosting code!-  {} - Hint for diagnosting code!'.format(b))
    word_of_user = str(input('Enter a word: ')) # Строковый тип т.к. мы же не знаем, что конкретно и какого типа содержится в списке!
    x = function_to_chooce_word
    if word_of_user == x:
            #print('YES, you guessed it!!!')
            Congratulations_1()

    else:
        print('No, you are wrong, word was "{}"'.format(function_to_chooce_word))
        print('See you next time!')

def gues_the_leter():
    b = splited_word
    print('Hint for diagnosting code!-  {} - Hint for diagnosting code!'.format(b))
    print('You have 3 possibilities to guess the letter!')
    match = 'Sorry, here no matches in our list!'
    guessesTaken = 0
    for guessesTaken in range(3):
        leter_of_user = str(input('Ok, enter a leter: '))
        for i in b: # Сравниеваем элименты списка с введенной буквой пользователя!
            if i == leter_of_user:
                Congratulations_2()
                for n, i in enumerate(b): # Создаем новый скрытый лист!
                    if i == leter_of_user:
                        new_hidden_list[n] = leter_of_user
                        print (new_hidden_list)
    print('You used all the attempts to guess letters! Now you have only one opportunity to guess the word!')
    gues_the_word()
    #if i != leter_of_user:
        #print(match)

def try_again():
    print('Do you wanna try again?')
    answer = input("Yes or No? >>> ")
    if answer.lower() == 'yes' or answer.lower() == 'y':
        gues_the_leter()
        function_to_chooce_word()
    elif answer.lower() == 'no' or answer.lower() == 'n':
        print("Thanks for game! See you next time!" )
        running = False

def counting_items_in_list():
    get_numbers_eliments_list = counting_items_in_the_list()
    return counting_items_in_list

"""--------------------Main body---------------------"""

print('Let\'s play to the "Gues the word"?')

answer = input("Yes or No? >>> ")
if answer.lower() == 'yes' or answer.lower() == 'y':
    print('Do you try to guess the whole word or try to guess the letter?')
    print('If you want to say the word enter the letter "W"')
    print('If you want to say the letter enter "L"')
    answer_of_user = str(input('What do you choose? >>> '))
    running = True
    while running:
        if answer_of_user.lower() == 'w':
            gues_the_word()
            running = False
        elif answer_of_user.lower() == 'l':
            gues_the_leter()
            break
        else:
            continue
        break
elif answer.lower() == 'No' or answer.lower() == 'n':
    print('Ok, Thank you for game! See you nex time!')

else:
    print("Sorry, I don't understand what you mean!")
    print("Ok! See you next time!" )
    running = False
