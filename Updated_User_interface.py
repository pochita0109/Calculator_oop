from User_interface import UserInterface

class Updated_User_interface(UserInterface):
    def name_input(self):
        name = input("\033[95m\033[1mPlease enter your name: ")
        return name
    
    def print_sum(self, sum, name):
        print("\033[92m\033[1mHey " + str(name) + ", " + "The sum is " + str(sum))

    def print_difference(self, difference, name):
        print("\033[92m\033[1mHey " + str(name) + ", " + "The difference is " + str(difference))
    
    def print_product(self, product, name):
        print("\033[92m\033[1mHey " + str(name) + ", " + "The product is " + str(product))
    
    def print_quotient(self, quotient, name):
        print("\033[92m\033[1mHey " + str(name) + ", " + "The quotient is " + str(quotient))