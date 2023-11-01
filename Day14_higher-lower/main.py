from art import logo, vs
from game_data import data
import random


# function to choose random item from game_data
def get_item_for_compare():
    random_item = random.choice(data)
    return random_item


# function to compare value of the two comparison choices and determine which is higher
def compare_items(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "a"
    elif a["follower_count"] == b["follower_count"]:
        return "Tie"
    else:
        return "b"


# function to evaluate if user's choice is correct
def check_user_is_correct(choice):
    result = compare_items(first_item, second_item)
    if result == choice:
        return "Correct"
    elif result == "Tie":
        return "Tie"
    else:
        return "Incorrect"


print(logo)

player_score = 0
continue_game = True
while continue_game:

    first_item = get_item_for_compare()
    second_item = get_item_for_compare()

    print(f"Compare A: {first_item["name"]}, a {first_item["description"]} from {first_item["country"]}")

    print(vs)
    print(f"Against B: {second_item["name"]}, a {second_item["description"]} from {second_item["country"]}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    round_result = check_user_is_correct(user_choice)
    if round_result == "Correct":
        player_score += 1
        print()
        print(f"\tYou're right! Current Score: {player_score}")
        print()
    elif round_result == "Tie":
        print()
        print(f"Tie. Current Score: {player_score}")
        print()
    else:
        print()
        print(f"\tSorry, that's wrong. Final Score: {player_score}")
        continue_game = False
