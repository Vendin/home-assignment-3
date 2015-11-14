import math
from decimal import Decimal

class Calculator:
    def addition(self, x, y):
        return float(Decimal(str(x)) + Decimal(str(y)))

    def subtraction(self, x, y):
        return float(Decimal(str(x)) - Decimal(str(y)))

    def multiply(self, x, y):
        return float(Decimal(str(x)) * Decimal(str(y)))

    def divide(self, x, y):
        if y == 0:
            raise ValueError('ZeroDivisionError')
        return float(Decimal(str(x)) / Decimal(str(y)))

    def logMy(self, x, y = math.e):
        if y <= 0 or x <= 0:
            raise ValueError('math domain error')
        if y == 1:
            raise ZeroDivisionError('float division by zero')
        z = 0
        if x < 1:
            x = x ** -1
            while (x - (y ** z)) >  0.000001:
                z += 0.000001
            return -round(z, 5)
        else:
             while (x - (y ** z)) >  0.000001:
                z += 0.000001
             return round(z, 5)

    def logMath(self, x, y):
        return math.log(x, y)

