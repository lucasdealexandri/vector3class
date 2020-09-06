#pylint: disable=not-an-iterable

import math
from typing import Union
import mathutils


class Vector3:

    '''
    A Vector object that has the properties mathematical vectors have:

    Vector addition / subtraction. e.g. Vector3(1, 2, 3) + Vector3(4, 5, 6) == Vector3(5, 7, 9)

    Scalar multiplication e.g. 2 * Vector3(1, 2, 3) == Vector3(2, 4, 6)

    Vector multiplication: a * b for dot product and a ** b for cross product
    (Alternatively, one could use a.dot(b) and a.cross(b) to explicitly effectuate the operations)

    Vector equality: Two vectors are the same if all their components are the same.

    Vector comparison: It compares the norms of the vectors. e.g. Vector3(1, 2, 3).norm == sqrt(14)
    Vector3(1, 2, 2).norm == 3; Vector3(1, 2, 3) > Vector3(1, 2, 2) == True

    Vector representation: Vector3(1, 2, 3) returns 1i + 2j + 3k (WIP)
    '''

    def __init__(self, *args: Union[list, tuple]):

        self.args = args

        if len(args) > 0: self.x = args[0]
        else: self.x = 0

        if len(args) > 1: self.y = args[1]
        else: self.y = 0

        if len(args) > 2: self.z = args[2]
        else: self.z = 0

        self.values = (self.x, self.y, self.z)

    def __len__(self) -> int:

        return self.dimension

    def __abs__(self) -> float:

        return self.norm

    def __add__(self, other: Union[list, tuple, 'Vector3']) -> 'Vector3':

        if type(other) in (list, tuple):

            other = Vector3(*other)

        return self.vector_addition(other)

    def __radd__(self, other: Union[list, tuple, 'Vector3']) -> 'Vector3':

        return self.__add__(other)

    def __sub__(self, other: Union[list, tuple, 'Vector3']) -> 'Vector3':

        if type(other) in (list, tuple):

            other = Vector3(*other)

        return self.vector_subtraction(other)

    def __rsub__(self, other: Union[list, tuple, 'Vector3']) -> 'Vector3':

        return self.__sub__(other)

    def __mul__(self, other: Union[int, float, list, tuple, 'Vector3']) -> Union[int, float]:

        if type(other) in (int, float):

            return self.scalar_multiplication(other)

        if type(other) in (list, tuple):

            other = Vector3(*other)

        return self.dot(other)

    def __rmul__(self, other: Union[int, float, list, tuple, 'Vector3']) -> Union[int, float]:

        return self.__mul__(other)

    def __truediv__(self, other: Union[int, float, list, tuple, 'Vector3']) -> 'Vector3':

        if type(other) in (int, float):

            return self.scalar_division(other)

    def __pow__(self, other: Union[list, tuple, 'Vector3']) -> 'Vector3':

        if type(other) in (list, tuple):

            other = Vector3(*other)

        return self.cross(other)

    def __rpow__(self, other: Union[list, tuple, 'Vector3']) -> 'Vector3':

        return self.__pow__(other)

    def __eq__(self, other: Union[list, tuple, 'Vector3']) -> bool:

        if type(other) in (list, tuple):

            other = Vector3(*other)

        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __gt__(self, other: Union[int, float, list, tuple, 'Vector3']) -> bool:

        if type(other) in (list, tuple):

            other = Vector3(*other)

        if type(other) in (int, float):

            return self.norm > other

        return self.norm > other.norm
    
    def __lt__(self, other: Union[int, float, list, tuple, 'Vector3']) -> bool:

        if type(other) in (list, tuple):

            other = Vector3(*other)

        if type(other) in (int, float):

            return self.norm < other

        return self.norm < other.norm

    def __ge__(self, other: Union[int, float, list, tuple, 'Vector3']) -> bool:

        if type(other) in (list, tuple):

            other = Vector3(*other)

        if type(other) in (int, float):

            return self.norm >= other

        return self.norm >= other.norm
    
    def __le__(self, other: Union[int, float, list, tuple, 'Vector3']) -> bool:

        if type(other) in (list, tuple):

            other = Vector3(*other)

        if type(other) in (int, float):

            return self.norm <= other

        return self.norm <= other.norm

    def __repr__(self) -> str:

        return str(self.values)

    def __str__(self) -> str:

        return str(self.values)

    def __iter__(self) -> 'tuple_iterator':

        return self.values.__iter__()

    def __getitem__(self, key) -> Union[int, float]:

        return self.values[key]

    def angle(self, other: 'Vector3', degree: bool = False, pretty_print: bool = False) -> Union[float, str]:

        angle_radians = math.acos(self.dot(other) / (self.norm * other.norm))
        angle_degrees = 180 / math.pi * angle_radians

        if degree:

            if pretty_print:

                return f'{angle_degrees:.2f}º'

            return mathutils.closestnum(angle_degrees)

        if pretty_print:

            return f'{angle_radians:.3f} rad'

        return mathutils.closestnum(angle_radians)

    def normalize(self) -> 'Vector3':

        normalized = tuple(mathutils.closestnum(a / self.norm) for a in self)

        return Vector3(*normalized)

    def scalar_multiplication(self, other: Union[int, float]) -> 'Vector3':

        scaled_components = tuple(mathutils.closestnum(a * other) for a in self)

        return Vector3(*scaled_components)

    def scalar_division(self, other: Union[int, float]) -> 'Vector3':

        scaled_components = tuple(mathutils.closestnum(a / other) for a in self)

        return Vector3(*scaled_components)

    def vector_addition(self, other: 'Vector3') -> 'Vector3':

        summed_components = tuple(mathutils.closestnum(a + b) for a, b in zip(self, other))

        return Vector3(*summed_components)

    def vector_subtraction(self, other: 'Vector3') -> 'Vector3':

        subtracted_components = tuple(mathutils.closestnum(a - b) for a, b in zip(self, other))

        return Vector3(*subtracted_components)

    def dot(self, other: 'Vector3') -> float:

        dot_product = sum(a * b for a, b in zip(self, other))

        return mathutils.closestnum(dot_product)

    # Still not scalable (Only works for 3D/2D vectors)
    def cross(self, other: 'Vector3') -> 'Vector3':

        x = mathutils.closestnum(self.y * other.z - self.z * other.y)
        y = mathutils.closestnum(self.z * other.x - self.x * other.z)
        z = mathutils.closestnum(self.x * other.y - self.y * other.x)

        return Vector3(x, y, z)

    @property
    def dimension(self) -> int:

        dimensions = 0

        for component in self.args:

            if component != 0:

                dimensions += 1

        return dimensions

    @property
    def norm(self) -> float:

        components_square = tuple(component ** 2 for component in self)

        return mathutils.closestnum(math.sqrt(sum(components_square)))

    def pprint(self) -> None:
        
        # This is a mess I am so sorry
        
        variables = []
        signs = []
        pprint_string = ''

        if self.x != 0:
            
            if self.x in (-1, 1): x = 'i'
            else: x = f'{abs(mathutils.closestnum(self.x))}i'
            
            if self.x < 0: signs.append(' - ')
            else: signs.append(' + ')
                
        else: 
            
            x = ''
            signs.append('')
            
        variables.append(x)
        
        if self.y != 0:
            
            if self.y in (-1, 1): y = 'j' 
            else: y = f'{abs(mathutils.closestnum(self.y))}j'
            
            if self.y < 0: signs.append(' - ')
            else: signs.append(' + ')
                
        else: 
            
            y = ''
            signs.append('')
            
        variables.append(y)
        
        if self.z != 0:
            
            if self.z in (-1, 1): z = 'k'
            else: z = f'{abs(mathutils.closestnum(self.z))}k'
            
            if self.z < 0: signs.append(' - ')
            else:signs.append(' + ')
                
        else: 
            z = ''
            signs.append('')
        
        variables.append(z)
        
        if len(variables) == 0:
            
            print('null vector')
            return None
        
        signs = [sign for sign in signs if sign != '']
        variables = [variable for variable in variables if variable != '']
            
        if signs[0] == ' + ': signs[0] = ''
        elif signs[0] == ' - ': signs[0] = '-'
        
        for i in range(len(variables)):
            
            pprint_string += signs[i] + variables[i]
    
        print(pprint_string)
        return None


class MagAngle(Vector3):

    '''
    MagAngle == Magnitude and Angle.
    Get a Vector3 object giving the norm of the vector and the angle with the horizon.
    Currently only works with 2D vectors (Because it only asks for one angle).
    '''

    def __init__(self, norm: Union[int, float], angle: Union[int, float] = 0, degree: bool = False):
        
        if degree:
            
            angle = math.radians(angle)

        x = mathutils.closestnum(norm * math.cos(angle))
        y = mathutils.closestnum(norm * math.sin(angle))

        super().__init__(x, y)


def angle(a: 'Vector3', b: 'Vector3', degree: bool = False) -> Union[int, float]:

    if degree:
        
        return a.angle(b, degree=True)

    return a.angle(b)

if __name__ == '__main__':

    a = [1, 2, 3]
    v1 = Vector3(*a)
    v2 = Vector3(1, 3, 2)

    print((1, 2) > Vector3(1, 2, 3))