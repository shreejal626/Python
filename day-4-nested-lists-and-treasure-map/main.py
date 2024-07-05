#states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa" "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#states_of_america[1] = "Pennsilvania" #changes the name of the item in the list

#states_of_america.append("Shreejal") #adds a single item to the end of the list

#states_of_america.extend(["shreejal", "maharjan"]) #adds a list to the end of the list

#print(states_of_america)

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#fruits = ["Strawberries", "Nectarines", "Apples", "Grapes" , "Peaches", "Cherries", "Pears"]
#vegetables = [ "Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#dirty_dozen = [fruits, vegetables]

#print(dirty_dozen[0][1]) #prints the second item in the first list

#print(dirty_dozen[1][3]) #prints the fourth item in the second list

dirty_dozen[1][3] = "Mango" #changes the fourth item in the second list to Mango

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower() #takes the first letter of the input and makes it lowercase
abc = ["a", "b", "c"] #list that represents the 3 possibilities for the first letter of the input
letter_index = abc.index(letter) #finds the index of the letter in the list
number_index = int(position[1]) - 1 #finds the index of the number in the list
map[number_index][letter_index] = "X" #in nested lists we go from outside to in, that means it checks for the corresponding list first, then the index of the item in that list

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")