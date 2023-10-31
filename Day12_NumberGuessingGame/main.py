import random

rand_num = int(random.randrange(0, 100))

print("Welcome to the random number guessing game.")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


def set_difficulty(user_difficulty):
    if user_difficulty == "easy":
        return 10
    else:
        return 5


def check_guess(guess, random_number):
    if guess > random_number:
        return "Too high"
    elif guess < random_number:
        return "Too low"
    else:
        return f"Correct"


def change_turns_remaining(guess_result):
    if guess_result == "Too high" or guess_result == "Too low":
        return -1


continue_game = True
turns_remaining = set_difficulty(difficulty)

while continue_game and turns_remaining >= 1:
    user_guess = int(input("Please guess a number between 1 and 100: "))
    result = check_guess(user_guess, rand_num)

    if result == "Correct":
        print(f"\tThe random number was {rand_num}")
        print(f"\tYou guessed the number with {turns_remaining} turns left!")
        continue_game = False
    else:
        print(f"\t{result}")
        turns_remaining += change_turns_remaining(result)
        if turns_remaining >= 1:
            print(f"\tYou have {turns_remaining} turns left to guess the correct number.")
        else:
            print(f"\tGame Over. The correct number was {rand_num}")
