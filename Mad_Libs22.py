""" 
Mad Libs? Это когда тебя просят дать список слов (типа "твоя любимая песня", "название животного", "число"), а потом подставляют их во фразу и получается смешно ("Корова летит со скоростью 350 километров в час и поет "Бесаме мучо").
"""
import random
print('Let\'s play to the "Mad Libs"')
answer = input("Yes or No? >>> ")
import time

if answer.lower() == 'yes' or answer.lower() == 'y':
    running = True

    while running:
       some_song = input('What is your favorite song?  >>> ')
       print("Ok" )
       some_animal = input('Please name any animal!  >>> ')
       print("Ok, last question!" )
       some_number = input('Say please any number!  >>> ')
       print('The {} flies at a speed of {} kilometers per hour and sings {}'.format(some_animal, some_number, some_song))
       print("Do you wont to continue Y/N")
       cont = input('>>> ')
       if cont.lower() == 'yes' or cont.lower() == 'y':
           print("I'm happy what you like it!")
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
