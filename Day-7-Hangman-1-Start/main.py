import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

random_choice = random.choice(word_list)

#print(random_choice)

guess = input("Enter a letter: ").lower()
if len(guess) >1 or len(guess)<=0 or guess.isnumeric():
 print("Ïnvalid Input")
else:
# print(guess)

 for a in random_choice:
  if a == guess:
   print("right")
  else:
   print("wrong")