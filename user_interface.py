# class userinterface
class UserInterface:
    
    # def ask_operation
    def ask_operation(self):
        operation = input(f" > > >  1. Addition 2. Subtraction 3. Multiplication 4. Division   < < < \nChoose the number of math operation you would like to use:  ").strip()
        # execute this when there is an exception
        if operation != "1" and operation != "2" and operation != "3" and operation != "4":
                raise ValueError("Invalid Input.")
        else:
            return operation
        
 