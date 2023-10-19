rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

user_input = int(input())
options = [0, 1, 2]
options_str = [rock, paper, scissors]
begin_game = 1

while begin_game == 1:
    if user_input in options:
        if user_input == 0:
            print(options_str[user_input])
            begin_game = 0
        elif user_input == 1:
            print(options_str[user_input])
            begin_game = 0
        elif user_input == 2:
            print(options_str[user_input])
            begin_game = 0
    else:
        print("User input is not valid. Please type 0 for Rock, 1 for Paper or 2 for Scissors.")
        user_input = int(input())
        begin_game = 1

    comp_choice = random.randint(0, len(options) -1)
    print(f"Computer chose: {options_str[comp_choice]}")

    results = [user_input, comp_choice]

    if results == [0,0] or results == [1,1] or results == [2,2]:
        print("Tie. What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
        user_input = int(input())
        begin_game = 1
    elif results == [0,2] or results == [1,0] or results == [2,1]:
        print("You win!")
        begin_game = 0
    else:
        print("You lose.")
        begin_game = 0
