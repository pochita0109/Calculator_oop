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