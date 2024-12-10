import random

word_list = ("ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra", "cougar",
             "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog", "goat",
             "goose", "hawk", "lion", "lizard", "llama", "mole", "monkey", "moose", "mouse", "mule", "newt",
             "otter", "owl", "panda", "parrot", "pigeon", "python", "rabbit", "ram", "rat", "raven",
             "rhino", "salmon", "seal", "shark", "sheep", "skunk", "sloth", "snake", "spider",
             "stork", "swan", "tiger", "toad", "trout", "turkey", "turtle", "weasel", "whale", "wolf",
             "wombat", "zebra")

def display_progress(word, correct_guesses):
    display = ''.join(letter if letter in correct_guesses else '_' for letter in word)
    print("Current word:", " ".join(display))

def main():
    word = random.choice(word_list)
    turns = 6
    correct_guesses = set()
    guessed_letters = set()

    print("Welcome to Hangman! I have picked my word, try and guess it:")

    while turns > 0:
        display_progress(word, correct_guesses)
        user_guess = input("Guess a letter: ").lower()

        if user_guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(user_guess)

        if user_guess in word:
            correct_guesses.add(user_guess)
            print(f"Good guess! '{user_guess}' is in the word.")
        else:
            turns -= 1
            print(f"Incorrect! '{user_guess}' is not in the word. Turns left: {turns}")

        if all(letter in correct_guesses for letter in word):
            print(f"CONGRATS! You've guessed the word: {word}!")
            break
    else:
        print(f"Out of turns! The word was: {word}")

if __name__ == "__main__":
    main()