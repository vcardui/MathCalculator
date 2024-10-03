#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Dictionary
operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
  "/": divide
}

def calculator():
  from art import logo
  print(logo)

  calculator_is_alive = True

  right_type = False
  while right_type == False:
    old_answer = input("What's the first number? ")
    
    if old_answer.replace(".","").isdigit():
      old_answer = float(old_answer)
      right_type = True
    else:
      print("   Please type a valid answer: ")

  while calculator_is_alive == True:
    for symbol in operations:
      print(symbol)

    right_type = False
    while right_type == False:
      operation_symbol = input("Pick an operator from the list above: ")

      in_the_list = False
      for symbol in operations:
        if operation_symbol == symbol:
          in_the_list = True
      
      if in_the_list == True:
        right_type = True

          
    calculation_function = operations[operation_symbol]

    right_type = False
    while right_type == False:
      num2 = input("What's the second number? ")

      if num2.replace(".","").isdigit():
        num2 = float(num2)
        right_type = True
      else:
        print("   Please type a valid answer: ")    

    if operation_symbol == '/' and num2 == 0:
      from art import eleventh_commandment
      print(eleventh_commandment)
    else:
      new_answer = calculation_function(n1 = old_answer, n2 = num2)
      print(f"\n{old_answer} {operation_symbol} {num2} = {new_answer}\n")

      valid_answer = False
      while valid_answer == False:
        user_choice = input(f"- Type 'continue' to keep calculating with {new_answer}\n- Type 'clear' to start a new calculation \n- Type 'exit' to exit: \n ").lower()

        if user_choice == 'continue':
          calculator_is_alive = True
          valid_answer = True

        elif user_choice == 'clear':
          calculator_is_alive = False
          calculator()
          valid_answer = True

        elif user_choice == 'exit':
          from art import bye
          print(bye)
          calculator_is_alive = False
          valid_answer = True

        else:
          print("   Please type a valid answer: ")

      old_answer = new_answer

calculator()