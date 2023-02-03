import random


def baseball_game():
    # generate random 3-digit number
    target = random.sample(range(1, 10), 3)
    target = "".join(map(str, target))
    print("Welcome to the number baseball game!")
    print("I have a 3-digit number in mind. Try to guess it.")
    print("You have 10 chances. Good luck!")

    strikes = 0
    balls = 0
    tries = 0

    while strikes < 3 and tries < 10:
        guess = input("Enter your guess: ")
        strikes, balls = check_guess(guess, target)
        tries += 1
        print("Strikes:", strikes, "Balls:", balls)
    if strikes == 3:
        print("You won! The target was", target)
    else:
        print("Sorry, you lost. The target was", target)


def check_guess(guess, target):
    strikes = 0
    balls = 0
    for i in range(3):
        if guess[i] == target[i]:
            strikes += 1
        elif guess[i] in target:
            balls += 1
    return strikes, balls


baseball_game()
