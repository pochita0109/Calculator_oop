# Kenneth John Costa
# Assignment 7
# Calculator in OOP

from User_interface import UserInterface
from Calculator import calculator

ui = UserInterface()
calcu = calculator()

while True:
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
    elif user_operation == 2:
        difference = calcu.subtraction(first_number, second_number)
        ui.print_difference(difference)
# If multiplication:
    elif user_operation == 3:
        product = calcu.multiplication(first_number, second_number)
        ui.print_product(product)
# If division:
    elif user_operation == 4:
        quotient = calcu.division(first_number, second_number)
        ui.print_quotient(quotient)
    else:
        print("ERROR! CHOOSE FROM 1-4")
# Ask the user if they want to try again
    if not ui.try_again():
        break