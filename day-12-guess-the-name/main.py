import random
import art
import replit

print(art.logo)

def number_of_attempts(difficulty):
  if difficulty == "easy":
    attempts = 10
  else:
    attempts = 5 
  return attempts

def random_choice():
  numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
   
  return random.choice(numbers_list)

def new_game():
  new_game = input("New game?: ")
  if new_game == "y":
    replit.clear()
    print(art.logo)
    guess_number()

def check_number(user_guess, random_number, attempts):
  if user_guess > random_number and attempts == 0:
    print("Too High\nYou've run out of guesses, you lose.")
  elif user_guess < random_number and attempts == 0:
    print("Too Low\nYou've run out of guesses, you lose.")
  elif user_guess > random_number:
    print("Too High\nGuess Again!")
  elif user_guess < random_number:
    print("Too Low\nGuess Again!")

def guess_number():
  
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")
  random_number = random_choice()
  print(f"Pssst, the correct answer is {random_number}")
  
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  attempts = number_of_attempts(difficulty)  
  
  is_match = False
  while not is_match and attempts > 0:   
    print(f"You have {attempts} attempts ramaining")
    attempts -=1
    user_guess = int(input("Make a guess: "))
    if user_guess == random_number:
      print(f"You got it! The answer was {random_number}.")
      is_match = True
    else: 
      check_number(user_guess, random_number, attempts)

  new_game()
    
guess_number()