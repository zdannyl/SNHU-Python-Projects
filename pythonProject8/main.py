import random

userName = str(input('Hello! Please enter your name: '))
print('Hello, {}! Welcome to the number guessing game.'.format(userName))

userRange = ''
while True:
    lower = int(input('Enter your lower number: '))
    upper = int(input('Enter your higher number: '))
    if lower > upper:
        print('Your first number must be smaller than your second number. Try again')
    if lower < upper:
        break

print('{}, your range is between {} and {}!'.format(userName, lower, upper))

randomNumber = random.randint(lower, upper)

guesses = 1
while True:
    userGuess = int(input('Enter your guess: '))
    if userGuess == randomNumber:
        print('{} was the correct number! It took {} tries!'.format(userGuess, guesses))
        break
    elif userGuess < randomNumber:
        print('{} is below the correct number. Try again:'.format(userGuess))
    elif userGuess > randomNumber:
        print('{} is above the correct number. Try again:'.format(userGuess))
    guesses += 1
