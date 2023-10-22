import random
from hangman_words import word_list
from hangman_art import stages, logo

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
lives = 6

print(f"{logo}")

# print(f"Chosen word: {chosen_word}")
letter_list = list(chosen_word)

display = []
for _ in chosen_word:
    display += "_"

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

# Check if letter has been guessed previously
    if guess in display:
        print(f"You've already guessed {guess}.")

# Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"Guessed letter {guess} was not found in the word. You've lost a life.")
        print(f"Lives remaining: {lives}")
        print()

        if lives == 0:
            game_over = True
            print("You lose")
            print(f"The word was: {chosen_word}")

    print(f"{' '.join(display)}")

    if '_' not in display:
        game_over = True
        print("You win!")

    print(stages[lives])
