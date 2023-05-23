# Kenneth John Costa
# Assignment 7
# Calculator in OOP

from User_interface import UserInterface
from Calculator import calculator

ui = UserInterface()
calcu = calculator()

# Ask the user to enter the first number
first_number = ui.input_first()
# Ask the user to enter the second number
second_number = ui.input_second()
# Ask the user about the operation they want to use 
user_operation = ui.choose_operation()
# If addition:
if user_operation == 1:
    sum = calcu.addition(first_number, second_number)
    ui.print_sum(sum)
# If subraction:
if user_operation == 2:
    difference = calcu.subtraction(first_number, second_number)
    ui.print_difference(difference)
# If multiplication:
if user_operation == 3:
    product = calcu.multiplication(first_number, second_number)
    ui.print_product(product)
# If division:
if user_operation == 4:
    quotient = calcu.division(first_number, second_number)
    ui.print_quotient(quotient)
# Ask the user if they want to try again