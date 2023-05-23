# Kenneth John Costa
# Assignment 7
# Calculator in OOP

from User_interface import UserInterface
from Calculator import calculator

ui = UserInterface()
calcu = calculator()

while True:
    first_number = ui.input_first()
    second_number = ui.input_second() 
    user_operation = ui.choose_operation()

    if user_operation == 1:
        sum = calcu.addition(first_number, second_number)
        ui.print_sum(sum)

    elif user_operation == 2:
        difference = calcu.subtraction(first_number, second_number)
        ui.print_difference(difference)

    elif user_operation == 3:
        product = calcu.multiplication(first_number, second_number)
        ui.print_product(product)

    elif user_operation == 4:
        quotient = calcu.division(first_number, second_number)
        ui.print_quotient(quotient)
    else:
        print("ERROR! CHOOSE FROM 1-4")

    if not ui.try_again():
        break