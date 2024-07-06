#For Loop
print("Enter student heights separated by a space.")
student_heights = input().split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#Solution using for loop to get the total of all the numbers in a list
total_height = 0

for heights in student_heights:
  total_height += heights
print(f"\ntotal height = {total_height}")

#Solution using for loop to get the number of items on a list
total_students = 0

for students in student_heights:
  total_students += 1
print(f"number of students = {total_students}")

#Solution to get average
average_height = 0
print(f"average height = {round(total_height/total_students)}")

#Solution using for loop to get the max item in a list
max_height = 0

for height in student_heights:
  if height > max_height:
    max_height = height  
print(f"max height = {max_height}\n")

#Solution to sum all the even number using for loop and range() function
print("Enter a number between 0 - 1000 to print out the sum of even numbers between 0 and the number:")
target = int(input())
if target%2 == 0:
  original_target = target
  target += 1  
  total_num = 0  
  for a in range(2, target, 2):
    total_num += a
  print(f"The sum of all the even numbers between 0 and {original_target} is = {total_num}")

  #another way of summing up even number:
  even_sum = 0
  for number in range(2, target + 1, 2):
    even_sum += number
  print(f"##result from another way = {even_sum}")
  
else:
  total_num = 0
  for a in range(2, target, 2):
    total_num += a
  print(f"The sum of all the even numbers between 0 and {target} is = {total_num}")

  #another way of summing up even number:
  even_sum = 0
  for number in range(2, target + 1, 2):
    even_sum += number
  print(f"##result from another way = {even_sum}")

#Solution to a FizzBuzz game. if divisible by 3 print Bizz, if divisible by 5 print Buzz, if divisible by 15 print FizzBuzz else print the number as is
for a in range(1, 101):
  if a%15 == 0:
    a = "FizzBuzz"
  elif a%3 == 0:
    a ="Fizz"  
  elif a%5 == 0:
    a = "Buzz"
  print(a)