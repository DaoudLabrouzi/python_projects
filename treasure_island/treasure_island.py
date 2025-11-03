"""
Treasure Island Adventure Game
Author: d.lbrzi
Description: A simple text-based game using conditionals and input handling.
"""

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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
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

# Write your code below this line 👇
game_over = True
the_Turn = input("You're in a cross road, do wanna turn Left or Right??").capitalize()
if the_Turn == "Right":
    print("Game over")
elif the_Turn == "Left":
    choice_2 = input("do you wanna swim or wait for the boat").capitalize()
    if choice_2 == "Swim":
        print("Game Over my friend you got eaten by a crocodaile")
    elif choice_2 == "Wait":
        choice_3 = input("right choice, now you arrived to the Island. \n You found a house with three doors, "
                         "one Red, Blue, and Yellow,\n which one you chose???").capitalize()
        if choice_3 == "Red":
            print("Game Over")
        elif choice_3 == "Yellow":
            print("Game Over")
        elif choice_3 == "Blue":
            print("You Win, You found the treasure")
