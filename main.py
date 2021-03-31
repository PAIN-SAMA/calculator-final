def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def divide(n1, n2):
  return n1 / n2
def multiply(n1, n2):
  return n1 * n2
operations = {'+':add,'-': subtract, '/': divide,'*': multiply}
def calculator():
  again = True
  num1 = float(input("What's the first number? "))
  while again:
    for any in operations:
      print(any)
    operation_symbols = input("Pick an operator from above ")
    num2 = float(input("What's the second number? "))
    calculation_function = operations[operation_symbols]
    answer = calculation_function(num1, num2) # num1 and num2 are replacing n1 and n2
    print(f" {num1} {operation_symbols} {num2} = {answer} ")
    end = input(f"'yes' to continue with the result {answer} or 'no' to begin another calculation? ")
    if end == 'yes':
      num1 = answer
    elif end == 'no':
      again = False
      calculator()
calculator()