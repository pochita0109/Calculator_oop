# Create a class for user interface
class UserInterface:
    def input_first(self):
        while True:
            try:
                first_number = float(input("Please enter the first number: "))
                return first_number
            except ValueError:
                print("ERROR! THE CHARACTER YOU HAVE ENTERED IS INVALID!")
    
    def input_second(self):
        while True:
            try: 
                second_number = float(input("Please enter the second number: "))
                return second_number
            except ValueError:
                print("ERROR! THE CHARACTER YOU HAVE ENTERED IS INVALID!")

    def choose_operation(self):
        while True:
            try:
                user_operation = int(input("Please enter the operation that you want to use (1,2,3,4): "))
                return user_operation
            except ValueError:
                print("ERROR! THE CHARACTER YOU HAVE ENTERED IS INVALID!")
    
    def print_sum(self, sum):
        print("The sum is " + str(sum))   

    def print_difference(self, difference):
        print("The difference is " + str(difference))     

    def print_product(self, product):
        print("The product is " + str(product))

    def print_quotient(self, quotient):
        print("The quotient is " + str(quotient))

    def try_again(self):
        while True:
            question = input("Type Y if you want to continue on using the simple calculator or N if not: ")
            if question.upper() == "Y":
                return True
            elif question.upper() == "N":
                print("THANK YOU FOR USING MY CALCULATOR!")
                return False
            else:
                print("ERROR! CHOOSE FROM Y OR N")
                continue