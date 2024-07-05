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

game_images = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input > 2 or user_input < 0:
    print("Invalid Input!")
else:    
    print(game_images[user_input])
    
    computer_choice = random.randint(0, len(game_images) - 1)
    
    print(game_images[computer_choice])
    
    
    if user_input == 0 and computer_choice == 2:
        print("You win.")
    elif user_input == 2 and computer_choice == 0:
        print("You lose.")
    elif user_input > computer_choice:
        print("You win.")
    elif computer_choice > user_input:
        print("You lose.")
    elif user_input == computer_choice:
        print("It's a draw.")