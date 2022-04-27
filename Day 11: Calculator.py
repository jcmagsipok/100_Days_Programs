#Calculator

#Add
def add(n1,n2):
  return n1 + n2
#Subtract
def subtract(n1,n2):
  return n1 - n2
#Multiply
def multiply(n1,n2):
  return n1 * n2
#Add
def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}  

function = operations["*"]
function(2,3)

def calculator():
  
  num1 = float(input("What's the first number?: "))
  should_continue = True
  
  for n in operations:
    print(n)
  should_continue = True
  
  while should_continue:
    symbol = input("Pick an operation from the above list: ")
    num2 = float(input("What's the next number?: "))
    calculation = operations[symbol]
    answer = calculation(num1,num2)
    print(f"{num1} {symbol} {num2} = {answer}")
    if input(f" Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

      
calculator()
