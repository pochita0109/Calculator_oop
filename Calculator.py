# Create a class for calculator
class calculator:
    def addition(self, first_number, second_number):
        sum = first_number + second_number
        return sum
    
    def subtraction(self, first_number, second_number):
        difference = first_number - second_number
        return difference
    
    def multiplication(self, first_number, second_number):
        product = first_number * second_number
        return product
    
    def division(self, first_number, second_number):
        while True:
            try:
                quotient = first_number / second_number
                return quotient
            except ZeroDivisionError:
                print("ERROR! YOU HAVE ZERO DIVISOR, PLEASE TRY AGAIN")
                break