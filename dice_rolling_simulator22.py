import random
print("Welcom to the game")
print("Do you want to start ?")
answer = input("Yes or No? >>> ")
import time

#if answer in['Yes', 'yes', 'y'] # проверяем если ответ есть в списке.
if answer.lower() == 'yes' or answer.lower() == 'y': #"ответ будет маленькими буквами! apper"
    running = True

    while running:
        dice = random.randint(1,6)
        print("Now you roll the dice!")
        time.sleep(1)
        print("Wate for it")
        time.sleep(1) # Задержка в секундах!
        print("Wate for it")
        time.sleep(1)
        print("-" * 10)
        print(dice)
        print("-" * 10)
        print("Do you wont to continue Y/N")
        cont = input('>>> ')

        if cont.lower() == 'yes' or cont.lower() == 'y':
            print('Rolling the dice again')
            running = True
        elif cont.lower() == 'no' or cont.lower() == 'n':
            print("Good game! See you next time!")
            running = False
        else:
            print("Sorry, I don't undestant it. Bye, bye")
            running = False

elif answer.lower() == 'no' or answer.lower() == 'n': 
    print("Thanks for game! See you next time!" )

else:
    print("Sorry, I dont't undestand you, Bye!")

