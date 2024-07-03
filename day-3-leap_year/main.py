print("Welcome to the leap year checker!\n")
year = int(input("Please enter a year: "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("This is a leap year!\n")
    else:
      print("This is not a leap year!\n")
  else:
    print("This is a leap year!\n")
else:
  print("This is not a leap year!\n")
print("Thank you! Have a nice day!")