import random
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

game_images = [rock, paper, scissors]

user_choice=int(input("What do you choose ? . Type 0 for ROCK , 1 for PAPER , 2 for SCISSORS "))
computer_choice=random.randint(0,2)
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])
print("computer chose : ")
print(game_images[computer_choice])
if user_choice>=3 or user_choice<0:
    print("You types an invalid option")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice> user_choice:
    print("you lose")
elif user_choice>computer_choice:
    print("you win")
elif computer_choice==user_choice:
    print("Its a draw")
else:
    print("You typed a invalid option")