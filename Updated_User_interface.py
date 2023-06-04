from User_interface import UserInterface

class Updated_User_interface(UserInterface):
    def name_input(self):
        name = input("Please enter your name: ")
        return name
    
    def print_sum(self, sum, name):
        print(str(name) + ", " + "The sum is " + str(sum))

    def print_difference(self, difference, name):
        print(str(name) + ", " + "The difference is " + str(difference))
    
    def print_product(self, product, name):
        print(str(name) + ", " + "The product is " + str(product))
    
    def print_quotient(self, quotient, name):
        print(str(name) + ", " + "The quotient is " + str(quotient))