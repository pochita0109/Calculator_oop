# Kenneth John Costa
# Assignment 7
# Calculator in OOP

from User_interface import UserInterface
from Calculator import calculator
from Updated_User_interface import Updated_User_interface

ui = UserInterface()
calcu = calculator()
Updated_ui = Updated_User_interface()

while True:
    name = Updated_ui.name_input()
    first_number = ui.input_first()
    second_number = ui.input_second() 
    user_operation = ui.choose_operation()

    if user_operation == 1:
        sum = calcu.addition(first_number, second_number)
        Updated_ui.print_sum(sum, name)

    elif user_operation == 2:
        difference = calcu.subtraction(first_number, second_number)
        Updated_ui.print_difference(difference, name)

    elif user_operation == 3:
        product = calcu.multiplication(first_number, second_number)
        Updated_ui.print_product(product, name)

    elif user_operation == 4:
        quotient = calcu.division(first_number, second_number)
        Updated_ui.print_quotient(quotient, name)
    else:
        print("\033[91m\033[1mERROR! CHOOSE FROM 1-4")

    if not ui.try_again():
        break