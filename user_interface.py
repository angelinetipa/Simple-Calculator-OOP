# class userinterface
class UserInterface:
    
    # def ask_operation
    def ask_user_operation(self):
        import time, os
        from colorama import Fore, Back, Style

        print(f"\n{Fore.BLACK}{Back.WHITE}{Style.BRIGHT}➕ ➖ ✖ ➗   S I M P L E     A P P     C A L C U L A T O R   ➗ ✖ ➖ ➕ {Style.RESET_ALL}")
        operation = ""
        while operation != "1" and operation != "2" and operation != "3" and operation != "4": 
            operation = input(f""" \n{Fore.MAGENTA}{Style.BRIGHT}> > >  1. Addition {Fore.GREEN}2. Subtraction {Fore.YELLOW}3. Multiplication {Fore.CYAN}4. Division   < < <
            \n{Style.RESET_ALL}Choose the number of math operation you would like to use:  """).strip()
            # execute this when there is an exception
            if operation != "1" and operation != "2" and operation != "3" and operation != "4":
                print (f"{Fore.RED}Invalid Input. Choose only the number from the given math operation ‼")
            else:
                return operation
            time.sleep(2.5)
            os.system("cls")    

    # def ask_2num
    def ask_user_number(self):
        number = float(input("Enter a number:  "))
        return number
    
    def display_sum(self, num1, num2, answer):
        from colorama import Fore, Style
        print(f"{Fore.MAGENTA}{num1} + {num2} = {Style.RESET_ALL}", answer)
    
    def display_difference(self, num1, num2, answer):
        from colorama import Fore, Style
        print(f"{Fore.GREEN}{num1} - {num2} = {Style.RESET_ALL}", answer)
     
    def display_product(self, num1, num2, answer):
        from colorama import Fore, Style
        print(f"{Fore.YELLOW}{num1} x {num2} = {Style.RESET_ALL}", answer)

    def display_quotient(self, num1, num2, answer):
        from colorama import Fore, Style
        print(f"{Fore.CYAN}{num1} / {num2} = {Style.RESET_ALL}", answer)

    # def last_message
    def display_last_message(self):
        from colorama import Style
        print(f"{Style.BRIGHT}\nThank you for using my Simple App Calculator! ♥{Style.RESET_ALL}\n ")