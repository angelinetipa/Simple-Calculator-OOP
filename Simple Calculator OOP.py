# import userinterface and calculator
from user_interface import UserInterface
from simple_calculator import SimpleCalculator

ui = UserInterface()
calc = SimpleCalculator()

# input for math operation
operation = ui.ask_operation()

# input for two numbers
num1, num2 = ui.ask_num()

# if math operation is addtion, output sum of two numbers
if operation == "1":
    calc.add()
# if math operation is subtraction, output difference of two numbers
# if math operation is multiplication, output product of two numbers
# if math operation is division, output quotient of two numbers
# input for try again