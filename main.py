import random

x = int(input("Let's play a game! Pick a number greater than 0: "))


def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print("Too low! Try again.")
        elif guess > random_num:
            print("Too high! Try again.")

    print(f"Look at you, stud muffin. You got {random_num} and beat me!")


print(guess(x))

print("Ok, now let's switch! You pick a number and I'LL guess it!")

y = int(input("I should guess between 1 and what other number? "))


def computer_guess(y):
    low = 1
    high = y
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f'Yay! I guessed {guess} correctly!')

print(computer_guess(y))
