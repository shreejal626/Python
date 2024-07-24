#calculator
import replit
import art



def add(n1, n2):
 return n1 + n2

def subtract(n1, n2):
 return n1 - n2

def multiply(n1, n2):
 return n1 * n2

def divide(n1, n2):
 return n1 / n2

operations = {
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide,
}


#tutor's version
def calculator():
 print(art.logo)
 num1 = float(input("What's your first number? : "))
 for symbol in operations:
  print(symbol)

 should_continue = True

 while should_continue:
  operation_symbol = input("Pick an operation: ")
  num2 = float(input("What's the next number? : "))
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")
  if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
   num1 = answer
  else:
   should_continue = False
   replit.clear()
   calculator()

calculator()


#my version

#num1 = int(input("What's the first number? : "))

# for symbol in operations:
#  print(symbol)
 
# operation_symbol = input("Pick an operation from the line above: ")

# num2 = int(input("What's the second number? : "))
# calcualtion_function = operations[operation_symbol]
# first_answer = calcualtion_function(num1, num2)

# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# repeat = True
# while repeat: 
#  result = input("continue? 'y' or 'n': ")
#  if result == "n":
#   repeat = False

#  elif result == "y":
#   operation_symbol = input("Pick an operation: ")
  
#   num3 = int(input("What's the next number? : "))
#   calculation_function = operations[operation_symbol]
#   second_answer = calculation_function(first_answer, num3)
   
#   print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
 
#   first_answer = second_answer 
