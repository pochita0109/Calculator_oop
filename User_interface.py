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
