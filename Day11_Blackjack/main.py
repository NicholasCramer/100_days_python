from art import logo
import random

""" Blackjack House Rules """
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


def deal_card():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand_card = random.choice(cards)

    return rand_card


def calculate_score(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0
    elif sum(hand) > 21 and 11 in hand:
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i] = 1
    return sum(hand)


def compare_score(player_score, comp_score):
    if player_score == 0:
        return "Blackjack! You win!"
    elif comp_score == 0:
        return "You lose! Computer got a Blackjack."
    elif player_score > 21:
        return "You went over 21. You lose!"
    elif 21 >= player_score > comp_score or player_score < comp_score > 21:
        return "You win!"
    elif player_score < comp_score <= 21:
        return "You lose!"
    else:
        return "Tie!"


new_game = True
while new_game:

    player_hand = []
    computer_hand = []
    player_turn = True
    computer_turn = False

    print(logo)

    user_response = input("Would you like to play a game of blackjack? 'y' or 'n' ").lower()
    if user_response == 'y':

        while len(player_hand) < 2:
            player_hand.append(deal_card())

        hand_total = calculate_score(player_hand)
        print(f"\tYour cards: {player_hand}, current score: {hand_total}")

        while len(computer_hand) < 2:
            computer_hand.append(deal_card())

        print(f"\tComputer's first card: {computer_hand[0]}")
        computer_total = calculate_score(computer_hand)

        while player_turn:
            if hand_total > 21:
                player_turn = False
            elif hand_total == 0:
                player_turn = False
            else:
                user_response = input("Type 'y' to get another card, type 'n' to pass: ").lower()

                if user_response == 'y':
                    player_hand.append(deal_card())
                    hand_total = calculate_score(player_hand)
                    print(f"\tYour cards: {player_hand}, current score: {hand_total}")
                    print(f"\tComputer's first card: {computer_hand[0]}")
                else:
                    print(f"\tYou decide to hold.")
                    player_turn = False
                    computer_turn = True
                    print(f"\tYour final hand: {player_hand}, current score: {hand_total}")

        while computer_turn:
            if computer_total < 17:
                computer_hand.append(deal_card())
                computer_total = calculate_score(computer_hand)
            else:
                computer_turn = False
                print(f"\tComputer's hand: {computer_hand}, computer score: {computer_total}")

        print(compare_score(hand_total, computer_total))

        print()
        new_game_response = input("Would you like to play again? 'y' or 'n' ").lower()
        if new_game_response != 'y':
            new_game = False

    else:
        break
