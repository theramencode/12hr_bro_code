import random

print("Welcome to the Number Guessing game, enter the range of the number I should pick: ")

low = int(input("Low(whole number): "))
high = int(input("High(whole number): "))

number = random.randint(low,high)
guess = int(input("I have picked a number, what is your guess?: "))
guesses = []

while True:
    if guess > high or guess < low:
        print("Your number is out of range!")
        guesses.append(guess)
        guess = int(input("Guess again: "))
    elif guess == number:
        print("CORRECT!")
        guesses.append(guess)
        numguesses = len(guesses)
        print(f"It took you {numguesses} guesses, Nice Job!")
        break
    elif guess > number:
        print("TOO HIGH!")
        guesses.append(guess)
        guess = int(input("Guess again: "))
    elif guess < number:
        print("TOO LOW!")
        guesses.append(guess)
        guess = int(input("Guess again: "))