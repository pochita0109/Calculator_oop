# Create a class for user interface
class UserInterface:
    def input_first(self):
        while True:
            try:
                first_number = float(input("\033[94mPlease enter the first number: "))
                return first_number
            except ValueError:
                print("\033[91m\033[1mERROR! THE CHARACTER YOU HAVE ENTERED IS INVALID!")
    
    def input_second(self):
        while True:
            try: 
                second_number = float(input("\033[94mPlease enter the second number: "))
                return second_number
            except ValueError:
                print("\033[91m\033[1mERROR! THE CHARACTER YOU HAVE ENTERED IS INVALID!")

    def choose_operation(self):
        print("\033[93m=" * 90)
        print("\033[0mADDITION: \033[94m1".center(81))
        print("\033[0mSUBTRACTION: \033[91m2".center(85))
        print("\033[0mMULTIPLICATION: \033[92m3".center(87))
        print("\033[0mDIVISION: \033[95m4".center(81))
        print("\033[93m=" * 90)
        while True:
            try:
                user_operation = int(input("\033[96mPlease enter the operation that you want to use (1,2,3,4): "))
                return user_operation
            except ValueError:
                print("\033[91m\033[1mERROR! THE CHARACTER YOU HAVE ENTERED IS INVALID!")
    
    def print_sum(self, sum):
        print("\033[92m\033[1mThe sum is " + str(sum))   

    def print_difference(self, difference):
        print("\033[92m\033[1mThe difference is " + str(difference))     

    def print_product(self, product):
        print("\033[92m\033[1mThe product is " + str(product))

    def print_quotient(self, quotient):
        print("\033[92m\033[1mThe quotient is " + str(quotient))

    def try_again(self):
        while True:
            question = input("\033[93mType Y if you want to continue on using the simple calculator or N if not: ")
            if question.upper() == "Y":
                return True
            elif question.upper() == "N":
                print("\033[95m\033[1mTHANK YOU FOR USING MY CALCULATOR!")
                return False
            else:
                print("\033[91m\033[1mERROR! CHOOSE FROM Y OR N")
                continue