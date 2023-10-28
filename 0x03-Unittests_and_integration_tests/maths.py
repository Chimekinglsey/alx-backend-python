import math

class Maths:
    """ run basic test for commmon maths operations"""
    def __init__(self) -> None:
        pass

    def add (self, *numbers):
        for i in numbers:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError('Invalid input')
        return sum(numbers)
    
    def sub (self, a: int or float, b: int or float) -> int | float:
        if isinstance(a, int) or isinstance(a, float) and isinstance(b, int) or isinstance(b, float):
            return round(a - b, 2) if isinstance(a, float) or isinstance(b, float) else a - b
        else:
            raise TypeError('Invalid input')

    
    def mul (self, *nums):
       
        for i in nums:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError('Invalid input')
            
        product = 1
        for i in nums:
            product *= i
        return product
    
    def div(self, num: int, num2: int) -> int:
        """ returns the division of two numbers"""
        if (not isinstance(num, int) and not isinstance(num, float)) and (not isinstance(num2, int) and not isinstance(num2, float)):
            raise TypeError('Invalid input')
        elif num2 != 0:
            return num/num2
        else:
            raise ZeroDivisionError('Cannot divide by zero')
        
    def mod (self, num1: int, num2: int) -> int:
        if not isinstance(num1, int) and not isinstance(num2, int) and not isinstance(num1, float) and not isinstance(num2, float):
            raise TypeError('Invalid input')
        if num2 == 0:
            raise ZeroDivisionError("Can't divide by zero")
        return num1 % num2
    
    def pow (self, a:int, b:int) -> int:
        if type(a) == int or type(b) == int or type(a)== float or type(b) == float:
            return (a ** b)
        else:
            raise TypeError('Invalid input type')

