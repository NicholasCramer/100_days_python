import sys

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/' . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

"""
* 'You\'re at a crossroad. Where do you want to go? Type "left" or "right"'
* 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
* "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
* "It\'s a room full of fire. Game Over."
* "You found the treasure! You Win!"
* "You enter a room of beasts. Game Over."
* "You chose a door that doesn\'t exist. Game Over."
* "You get attacked by an angry trout. Game Over."
* "You fell into a hole. Game Over."
"""
print("What is your name? ")
name = input()

print(f"Welcome, {name}. Let's get started.")
print("")

print("You walk along a forest path. You see a crossroads up ahead. Do you go right or left?")
choice1 = input().upper().strip()
choice1_flag = False
stop_game = False

while choice1_flag == False:
    try:
        if choice1 == "RIGHT":
            print("You head down the right path.")
            choice1_flag = True
            stop_game = True
            print("A tree falls down and crushes you.")
        elif choice1 == "LEFT":
            print("You head down the left path.")
            choice1_flag = True
        else:
            print(f"You chose: {choice1}. Please choose either right or left.")
            choice1_flag = False
    finally:
        if stop_game == True:
            print("GAME OVER")
            sys.exit()
        elif choice1_flag == False:
            choice1 = input().upper().strip()
        else:
            print("You\'ve made it through the forest!")

print("There's a large lake in the clearing ahead. A dock waits at the end of the path.")
print("There are no boats in sight, but it looks like there was a boat here recently.")
print("Do you attempt to swim across the lake? Or wait for a boat? Swim or Wait")
choice2 = input().upper().strip()
choice2_flag = False

while choice2_flag == False:
    try:
        if choice2 == "SWIM":
            print("You start to swim across the lake.")
            choice2_flag = True
            print("A large tentacle rises from the water and grabs you. You're slowly pulled down into ")
            print("the murky depths of the lake.")
            stop_game = True
        elif choice2 == "WAIT":
            print("You wait for hours. Finally, a man in a boat appears. You offer him 1 gold coin to take ")
            print("you to the island in the middle of the lake.")
            choice2_flag = True
        else:
            print(f"You chose: {choice2}. Please choose either wait or swim.")
    finally:
        if stop_game == True:
            print("GAME OVER")
            sys.exit()
        elif choice2_flag == False:
            choice2 = input().upper().strip()
        else:
            print("You\'ve made it to the island!")

print("As you reach the island, you notice a large mansion that looks deserted.")
print("You open the front door and enter.")
print("Inside there is a large empty room with three exits: a red door, a blue door, and a yellow door.")
print("Which door do you choose? (Red, Yellow, Blue)")
choice3 = input().upper().strip()
choice3_flag = False

while choice3_flag == False:
    try:
        if choice3 == "RED":
            print("You open the red door.")
            print("It's a trap! A large pit opens up beneath you and you fall to your death.")
            choice3_flag = True
            stop_game = True
        elif choice3 == "YELLOW":
            print("You open the yellow door.")
            choice3_flag = True
        elif choice3 == "BLUE":
            print("You open the blue door.")
            print("It's a trap! A crossbow inside the room shoots you in the chest as the door swings open.")
            choice3_flag = True
            stop_game = True
        else:
            print(f"You chose: {choice3}. Please choose either red, yellow, or blue.")
    finally:
        if stop_game == True:
            print("GAME OVER")
            sys.exit()
        elif choice3_flag == False:
            choice3 = input().upper().strip()
        else:
            print("You\'ve found the treasure. Congratulations!")
            sys.exit()

