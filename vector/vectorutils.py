from typing import Union
from fractions import Fraction
import math

RealNumber = Union[int, float]

def closestint(result: float, tolerance: float = 1e-9) -> RealNumber:
    
    '''
    A function that balances float point precision.

    For instance: closestint(10.000000001) == 10. This is useful for a handful of
    functions in this class, especially those counting on square roots and trigonometric functions.

    However if the number is not withing the tolerance range from an integer,
    the function returns the number itself, without rounding
    For instance: closestint(1.0000122) == 1.0000122
    '''

    if abs(result - math.floor(result)) <= tolerance:

        return math.floor(result)

    if abs(result - math.ceil(result)) <= tolerance:

        return math.ceil(result)

    return result

def closestfloat(number: float) -> float:
    
    '''
    This function comes with the same purpose as closestint, however, as the name suggests,
    it targets floats. 
    
    For instance: closestfloat(1.2000000000000002) == 1.2
                  closestfloat(1.2999999999999999) == 1.3
    
    The way it works is by checking if there is a long string of 0's or 9's in the number. If it does, then
    there's a strong chance this is a floating point precision situation; so the function converts
    the number into a string, and split it where there's a lot of 0's or 9's; then takes the first item of
    the formed list, which should be the precise number for the case of 0's. For 9's it also changes the
    last digit before the long string of 9's to one digit up.
    '''
    
    if 6 * '9' in str(number):
        
        number_string = str(number).split(6 * '9')[0]
        
        last_digit = int(number_string[-1])
        new_last_digit = str(last_digit + 1)
        
        number_string = number_string[:-1] + new_last_digit
        
        return float(number_string)
        
    return float(str(number).split(6*'0')[0])

def closestnum(number: RealNumber) -> RealNumber:
    
    '''
    This function unifies closestint and closestfloat.
    '''
    
    number = closestint(closestfloat(number))
    
    return number

def where_is_pi(number: RealNumber, tolerance: float = 1e-7, limit_denominator: int = 200) -> str:
    
    fitting_pi = number / math.pi
    approximation = Fraction(fitting_pi).limit_denominator(limit_denominator)
    
    if -tolerance <= approximation - fitting_pi <= tolerance:
        
        return f'{approximation} pi'
    
    return number

if __name__ == '__main__':
    
    a = 2 / 300 * math.pi
    
    print(where_is_pi(a))