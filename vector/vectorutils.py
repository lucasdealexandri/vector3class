from typing import Union
from fractions import Fraction
from itertools import chain
import numpy as np
import math

RealNumber = Union[int, float]


def closestint(result: float, tolerance: float = 1e-9) -> RealNumber:
    '''
    A function that balances float point precision.

    For instance: closestint(10.000000001) == 10. This is useful for a handful of
    functions in the Vector3 class, especially those counting on square roots and trigonometric functions.

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
        if number_string[-1] == '.': number_string = number_string[:-1]

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


def where_is_pi(angle: RealNumber, tolerance: float = 1e-7, limit_denominator: int = 200) -> str:
    '''
    This function looks for a reasonable constant multiplying pi and make it obvious
    e.g. instead of displaying "2.0943951023931953", this function will display a nice
    "2/3 pi". Much friendlier huh?!
    '''

    angle = closestnum(essential_angle(angle))

    if angle == 0:

        return '0'

    fitting_pi = angle / math.pi
    approximation = Fraction(fitting_pi).limit_denominator(limit_denominator)

    if -tolerance <= approximation - fitting_pi <= tolerance:

        if approximation == 1:

            return 'pi'

        return f'{approximation} pi'

    return f'{angle}'


def essential_angle(angle: RealNumber) -> float:

    tau = 2 * math.pi

    return angle - angle // tau * tau


def prime_factors(number: int):

    factors = []

    while number % 2 == 0:
        factors.append(2)
        number /= 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):

        while number % i == 0:
            factors.append(i)
            number /= i

    if number > 2:
        factors.append(int(number))

    return factors


def pretty_sqrt(number: int) -> str:

    if number != int(number):

        return f'{number}'

    factors = prime_factors(number)
    in_sqrt = []
    out_sqrt = []

    while len(factors) > 1:

        if duplet(factors):

            out_sqrt.append(factors[0])
            remove_duplet(factors)

        else:

            in_sqrt.append(factors[0])
            factors.pop(0)

    if len(factors) == 1:

        in_sqrt.append(factors[0])
        factors.pop(0)

    out_sqrt = int(np.prod(out_sqrt))
    in_sqrt = int(np.prod(in_sqrt))

    if in_sqrt == 1:

        return f'{out_sqrt}'

    if out_sqrt == 1:

        return f'sqrt({in_sqrt})'

    return f'{out_sqrt} sqrt({in_sqrt})'


def duplet(factors: list) -> bool:

    return factors[0] == factors[1]


def remove_duplet(factors: list) -> None:

    factors.pop(0)
    factors.pop(0)


if __name__ == '__main__':

    a, b, c = (1, 1, 4)

    print(pretty_sqrt(a ** 2 + b ** 2 + c ** 2))
