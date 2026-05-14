print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

choice1 = input('You are at a crossroad where do you want to go ? '
                'TYPE - "Left" or "Right"\n').lower()

if choice1=="right":
    print("you fell into a hole . Game Over ")
else :
    choice2 = input("You hav come to a lake . "
                    "There is an Island in the middle of the lake ."
                    " Type 'Wait' to wait for a boat ."
                    " Type 'Swim' to swim across\n ").lower()
    if choice2=='wait':
        choice3= input("You arrive at the island unharmed ."
                       "There is a house with 3 doors , one yellow one blue and one red \n ").lower()
        if choice3=='red':
            print("Its a room full of fire . Game Over ")
        elif choice3=='blue':
            print('Its a room full of fire . Game Over')
        else : print("YOU FOUND THE TREASURE ! YOU WIN ! :)")


    else : print("You got attacked by an angry trout . Game Over :( ")
