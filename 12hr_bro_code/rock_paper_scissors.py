import random
import time

options = ("rock", "paper", "scissor")
running = True

print("-------------------------")
print()
print("Rochambeau")
print()
    
while running:
    print("-------------------------")
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissor")
    time.sleep(1)
    print("Shoot!")
    time.sleep(1)
    print("-------------------------")

    player = input("Player picks: ").lower()
    computer = random.choice(options)
    print(f"Computer picks: {computer}")
    print("-------------------------")

    if player == computer:
        print("IT'S A TIE!")
    elif player == "rock" and computer == "scissor":
        print("YOU WIN!")
    elif player == "paper" and computer == "rock":
        print("YOU WIN!")
    elif player == "scissor" and computer == "paper":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")

    play_again = input("Play again?(Y/N): ").lower()
    if play_again != "y":
        running = False
    print("Thanks for playing!")
