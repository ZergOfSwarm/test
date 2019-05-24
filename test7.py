import random
guessesTaken = 0
number = random.randint(1, 4)
print ('выбранное число',number)
for guessesTaken in range(6):
    print('Попробуй угадать.')
    guess = input('Введите число >>> ')
    guess = int(guess)

    if guess < number:
        print('Твое число слишком маленькое.')

    if guess > number:
            print('Твое число слишком большое.')

    if guess == number:
        break

if guess == number:
    print('You are WINNER!')
