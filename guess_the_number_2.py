import random
def Congratulations ():
    print('Congratulations,  You are WINNER!')
    print('WINNER, WINNER, WINNER, WINNER!')

def try_again():
    run = True
    while run:
        count = input('Do you wanna try again? >>> ')
        if count.lower() == 'yes' or count.lower() == 'y':
            print('You are welcom!')
            return True # От сюда переходит в основной цикл???
        if count.lower() == 'no' or count.lower() == 'n':
            print('Thanks for GAME! See you again!')
            break


"""------------------Main body-----------------------------------"""
#print("Welcom to the game")
user_name = input("Hi, what is your name? >>> ")
print('Nice to meet you {}!'.format(user_name))
print('Ill pick a number frome 1 to 6.')
answer = input("Try to guess it, do you want to start 'Yes or No'? >>> ")
if answer.lower() == 'yes' or answer.lower() == 'y':
    running = True

    while running:
        dice = random.randint(1,6)
        print(dice)
        user_input = int(input ("Try to guess a number! >>> "))

        if user_input > dice:
            print('Your number is too big.')
            running = try_again()
           # count = input('Do you wanna try again? >>> ')
           # if count.lower() == 'yes' or count.lower() == 'y':
           #     print('You are welcom!')
           #     running = True
           # else:
           #     print('Thanks for game {}! See you again!'.format(user_name))
           #     running = False

        if user_input < dice:
            print('Your number is too small.')
            running = try_again()
            #count = input('Do you wanna try again? >>> ')
            #if count.lower() == 'yes' or count.lower() == 'y':
            #    print('You are welcom!')
            #    running = True
            #else:
            #    print('Thanks for game {}! See you again!'.format(user_name))
            #    running = False

        if user_input == dice:
            Congratulations ()
            running = try_again()
            #count = input('Do you wanna try again? >>> ') 
            #if count.lower() == 'yes' or count.lower() == 'y':
            #    print('You are welcom!')
            #    running = True
            #else:
            #    print('Thanks for game {}! See you again!'.format(user_name))
            #    running = False

        #else:
        #    print('sorry, You are wrong! Number was',dice)
        #    count = input('Do you wanna try again? >>> ') 
        #    if count.lower() == 'yes' or count.lower() == 'y':
        #        print('You are welcom!')
        #        running = True
        #    else:
        #        print('Thanks for game {}! See you again!'.format(user_name))
        #        running = False
else: 
    print("Ok, I don't understand what you mean!!! But, I hope see you again!!")
    running = False


#Zorg adventure - посмотри, говорят не сложно! В книге будет ссылка на ресурс!:
