from simple_calculator import SimpleCalculator

class CalculatorTipa(SimpleCalculator):
    def remainder_ofdiv(self, num1, num2):
        remainder = num1 % num2
        return remainder
    
    def exponent(self, num1, num2):
        exponential_power = num1 ** num2
        return exponential_power