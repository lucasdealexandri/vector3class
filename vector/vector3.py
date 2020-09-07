#pylint: disable=not-an-iterable

import math
from typing import Union
from vectorutils import closestnum, where_is_pi, pretty_sqrt

RealNumber = Scalar = Union[int, float]
Coordinate = Union[list, tuple]
Vector = Union[list, float, 'Vector3']


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

    def __init__(self, *args: Coordinate):

        self.args = args

        if len(args) > 0:
            self.x = args[0]
        else:
            self.x = 0

        if len(args) > 1:
            self.y = args[1]
        else:
            self.y = 0

        if len(args) > 2:
            self.z = args[2]
        else:
            self.z = 0

        self.values = (self.x, self.y, self.z)

    def __len__(self) -> int:

        return self.dimension

    def __abs__(self) -> float:

        return self.norm

    def __add__(self, other: Vector) -> 'Vector3':

        if type(other) in (list, tuple):

            other = Vector3(*other)

        return self._vector_addition(other)

    def __radd__(self, other: Vector) -> 'Vector3':

        return self.__add__(other)

    def __sub__(self, other: Vector) -> 'Vector3':

        if type(other) in (list, tuple):

            other = Vector3(*other)

        return self._vector_subtraction(other)

    def __rsub__(self, other: Vector) -> 'Vector3':

        return self.__sub__(other)

    def __mul__(self, other: Union[Scalar, Vector]) -> RealNumber:

        if type(other) in (int, float):

            return self._scalar_multiplication(other)

        if type(other) in (list, tuple):

            other = Vector3(*other)

        return self.dot(other)

    def __rmul__(self, other: Union[Scalar, Vector]) -> RealNumber:

        return self.__mul__(other)

    def __truediv__(self, other: Union[Scalar, Vector]) -> 'Vector3':

        if type(other) in (int, float):

            return self._scalar_division(other)

    def __pow__(self, other: Vector) -> 'Vector3':

        if type(other) in (list, tuple):

            other = Vector3(*other)

        return self.cross(other)

    def __rpow__(self, other: Vector) -> 'Vector3':

        return self.__pow__(other)

    def __eq__(self, other: Vector) -> bool:

        if type(other) in (list, tuple):

            other = Vector3(*other)

        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __gt__(self, other: Union[Scalar, Vector]) -> bool:

        if type(other) in (list, tuple):

            other = Vector3(*other)

        if type(other) in (int, float):

            return self.norm > other

        return self.norm > other.norm

    def __lt__(self, other: Union[Scalar, Vector]) -> bool:

        if type(other) in (list, tuple):

            other = Vector3(*other)

        if type(other) in (int, float):

            return self.norm < other

        return self.norm < other.norm

    def __ge__(self, other: Union[Scalar, Vector]) -> bool:

        if type(other) in (list, tuple):

            other = Vector3(*other)

        if type(other) in (int, float):

            return self.norm >= other

        return self.norm >= other.norm

    def __le__(self, other: Union[Scalar, Vector]) -> bool:

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

    def __getitem__(self, key) -> RealNumber:

        return self.values[key]

    def angle(self, other: 'Vector3', degree: bool = False, pretty_print: bool = False) -> Union[float, str]:
        '''
        Returns the angle between two vectors
        e.g. Vector3(1, 2, 3).angle(Vector3(2, 4, 6)) == 0
        '''

        angle_radians = math.acos(self.dot(other) / (self.norm * other.norm))
        angle_degrees = 180 / math.pi * angle_radians

        if degree:

            if pretty_print:

                return f'{angle_degrees:.2f}º'

            return closestnum(angle_degrees)

        if pretty_print:
            
            if where_is_pi(angle_radians) != angle_radians:
                
                return f'{where_is_pi(angle_radians)} rad'

            return f'{angle_radians:.3f} rad'

        return closestnum(angle_radians)

    def normalize(self) -> 'Vector3':
        '''
        Returns a normalized vector, i.e. a vector with the same direction with norm (magnitude) == 1
        e.g. Vector3(2, 0, 0).normalize() == Vector3(1, 0, 0)
        '''

        normalized = tuple(closestnum(a / self.norm) for a in self)

        return Vector3(*normalized)

    def _scalar_multiplication(self, other: RealNumber) -> 'Vector3':
        '''
        Returns the multiplication between a vector and a scalar
        e.g. Vector3(1, 2, 3) * 2 == Vector3(2, 4, 6)
        '''

        scaled_components = tuple(closestnum(a * other) for a in self)

        return Vector3(*scaled_components)

    def _scalar_division(self, other: RealNumber) -> 'Vector3':
        '''
        Returns the division between a vector and a scalar
        e.g. Vector3(3, 6, 9) / 3 == Vector3(1, 2, 3)
        '''

        scaled_components = tuple(closestnum(a / other) for a in self)

        return Vector3(*scaled_components)

    def _vector_addition(self, other: 'Vector3') -> 'Vector3':
        '''
        Returns the sum of two vectors
        Namely a + b
        '''

        summed_components = tuple(closestnum(a + b)
                                  for a, b in zip(self, other))

        return Vector3(*summed_components)

    def _vector_subtraction(self, other: 'Vector3') -> 'Vector3':
        '''
        Returns the difference between two vectors
        Namely a - b
        '''

        subtracted_components = tuple(closestnum(a - b)
                                      for a, b in zip(self, other))

        return Vector3(*subtracted_components)

    def dot(self, other: 'Vector3') -> float:
        '''
        Returns the dot product between two vectors.
        Namely a • b
        Can be used as a * b in code.
        '''

        dot_product = sum(a * b for a, b in zip(self, other))

        return closestnum(dot_product)

    # Still not scalable (Only works for 3D/2D vectors)
    def cross(self, other: 'Vector3') -> 'Vector3':
        '''
        Returns the cross product between two vectors.
        Namely a x b
        Can be used as a ** b in code.
        '''

        x = closestnum(self.y * other.z - self.z * other.y)
        y = closestnum(self.z * other.x - self.x * other.z)
        z = closestnum(self.x * other.y - self.y * other.x)

        return Vector3(x, y, z)

    @property
    def dimension(self) -> int:
        '''
        The smallest dimension in which a vector could be represented:
        e.g. Vector3(3, 0, 0) can be represented in the number line, so it can be represented in at least one dimension.

        Vector3(1, 0, 2) for instance, might look like it needs to be 3D, but if you look closer you can see
        it can easly be represented in a plane, namely the XZ plane, so the smallest dimension it can be represented is 2.

        In short, all non zero values in the vector are accounted as a new dimension, so in order for a vector
        to be considered to have 3 dimensions, it needs 3 non-zero values.
        '''

        dimensions = 0

        for component in self.args:

            if component != 0:

                dimensions += 1

        return dimensions

    @property
    def norm(self) -> float:
        '''
        Returns the norm (magnitude) of the vector.
        '''

        components_square = tuple(component ** 2 for component in self)

        return closestnum(math.sqrt(sum(components_square)))

    def to_cylindrical(self) -> str:
        '''
        Outputs the cylindrical coordinate of the vector, and in a pretty manner.
        '''

        self.theta = closestnum(math.atan2(self.y, self.x))
    
        pretty_r = self.compact_radius()['r']
        pretty_theta = where_is_pi(self.theta)

        return f'({pretty_r}, {pretty_theta}, {self.z})'

    def to_spherical(self):
        '''
        Outputs the spherical coordinate of the vector, also in a pretty manner.
        '''

        sum_squared_components = sum(
            [components ** 2 for components in (self.x, self.y, self.z)])

        self.rho = closestnum(math.sqrt(sum_squared_components))
        self.theta = closestnum(math.atan2(self.y, self.x))
        self.phi = closestnum(math.acos(self.z / self.rho))

        pretty_rho = self.compact_radius()['rho']
        pretty_theta = where_is_pi(self.theta)
        pretty_phi = where_is_pi(self.phi)

        return f'({pretty_rho}, {pretty_theta}, {pretty_phi})'

    def component_output(self) -> str:
        '''
        Base for pretty printing; it returns a vector (a, b, c) in the form of
        ai + bj + ck. This function also accounts for zero valued components
        e.g. Vector3(1, 0, -4).beautify would return 1i - 4k
        '''

        # This is a mess I am so sorry

        variables = []
        signs = []
        pprint_string = ''

        if self.x != 0:

            if self.x in (-1, 1):
                x = 'i'
            else:
                x = f'{abs(closestnum(self.x))}i'

            if self.x < 0:
                signs.append(' - ')
            else:
                signs.append(' + ')

        else:

            x = ''
            signs.append('')

        variables.append(x)

        if self.y != 0:

            if self.y in (-1, 1):
                y = 'j'
            else:
                y = f'{abs(closestnum(self.y))}j'

            if self.y < 0:
                signs.append(' - ')
            else:
                signs.append(' + ')

        else:

            y = ''
            signs.append('')

        variables.append(y)

        if self.z != 0:

            if self.z in (-1, 1):
                z = 'k'
            else:
                z = f'{abs(closestnum(self.z))}k'

            if self.z < 0:
                signs.append(' - ')
            else:
                signs.append(' + ')

        else:
            z = ''
            signs.append('')

        variables.append(z)

        signs = [sign for sign in signs if sign != '']
        variables = [variable for variable in variables if variable != '']

        if len(variables) == 0:

            return 'null vector'

        if signs[0] == ' + ':
            signs[0] = ''
        elif signs[0] == ' - ':
            signs[0] = '-'

        for i in range(len(variables)):

            pprint_string += signs[i] + variables[i]

        return pprint_string

    def compact_radius(self) -> str:
        '''
        This function makes clear the presence of square roots, so the output
        of conversions to polar, cylindrical, and spherical coordinate vectors become nicer.
        
        For instance, the radius "r", used in cylindrical coordinates, for Vector3(1, 1, 1) is 1.414213...
        and the radius "rho", used in spherical coordinates, for the same vector is 1.732050...
        Both are, successively, sqrt(2) and sqrt(3), and this is how the function represents them.
        
        Also works for, for instance, the radius "rho" for Vector(1, 1, 4) is sqrt(18),
        which can also be represented as 3 sqrt(2), and this is how the function represents it.
        '''
        
        sum_squared_2d_components = closestnum(self.x ** 2 + self.y ** 2)
        sum_squared_3d_components = closestnum(self.x ** 2 + self.y ** 2 + self.z ** 2)
        
        r = pretty_sqrt(sum_squared_2d_components)
        rho = pretty_sqrt(sum_squared_3d_components)
        
        return {'r': r, 'rho': rho}

    def pprint(self) -> None:

        print(self.component_output())


class MagAngle(Vector3):

    '''
    MagAngle == Magnitude and Angle.
    Get a Vector3 object giving the norm of the vector and the angle with the horizon.
    '''

    def __init__(self, norm: RealNumber, angle: RealNumber = 0, degree: bool = False, polar_repr: bool = False):

        self.ang = angle

        self._polar_repr = polar_repr

        if degree:

            angle = math.radians(angle)

        self.x = closestnum(norm * math.cos(angle))
        self.y = closestnum(norm * math.sin(angle))

        super().__init__(self.x, self.y)

    def __str__(self) -> str:

        # Figure out a way to factor pi out and represent it.

        if self._polar_repr:

            pretty_angle = where_is_pi(self.ang)
            return f'({self.norm}, {pretty_angle})'

        return str((self.x, self.y))


class Polar(MagAngle):

    '''
    Polar form of a vector; essentially the same as MagAngle, but with "proper" notation.
    Returns a 2D Vector3 object (i.e. a Vector3 with the z component = 0).
    '''

    def __init__(self, r: RealNumber, theta: RealNumber = 0, degree: bool = False, polar_repr: bool = False):

        self.r = r
        self.theta = theta

        super().__init__(r, theta, degree, polar_repr)


class Cylindrical(Vector3):

    '''
    Cylindrical form of a vector: returns a Vector3 object based on the 
    cylindrical coordinate of the tip of the vector.
    The convention for r, theta and z are shown in this study guide:
    http://sites.science.oregonstate.edu/math/home/programs/undergrad/CalculusQuestStudyGuides/vcalc/coord/coord.html
    '''

    def __init__(self, r: RealNumber, theta: RealNumber, z: RealNumber, degree: bool = False, cylindrical_repr: bool = False):

        self.r = r
        self.theta = theta
        self.z = z

        self._cylindrical_repr = cylindrical_repr

        if degree:

            theta = math.radians(theta)

        self.x = closestnum(r * math.cos(theta))
        self.y = closestnum(r * math.sin(theta))

        super().__init__(self.x, self.y, self.z)

    def __str__(self) -> str:

        # Figure out a way to factor pi out and represent it.

        if self._cylindrical_repr:

            pretty_theta = where_is_pi(self.theta)

            return f'({self.r}, {pretty_theta}, {self.z}))'

        return str((self.x, self.y, self.z))


class Spherical(Vector3):

    '''
    Vector3 object based on the spherical coordinate of the tip of the vector
    Conventions for rho, theta and phi are based on the following study guide:
    http://sites.science.oregonstate.edu/math/home/programs/undergrad/CalculusQuestStudyGuides/vcalc/coord/coord.html
    '''

    def __init__(self, rho: RealNumber, theta: RealNumber, phi: RealNumber, degree: bool = False, spherical_repr: bool = False):

        self.rho = rho
        self.theta = theta
        self.phi = phi

        self._spherical_repr = spherical_repr

        if degree:

            rho = math.radians(rho)
            phi = math.radians(phi)

        self.x = closestnum(rho * math.sin(phi) * math.cos(theta))
        self.y = closestnum(rho * math.sin(phi) * math.sin(theta))
        self.z = closestnum(rho * math.cos(phi))

        super().__init__(self.x, self.y, self.z)

    def __str__(self) -> str:

        # Figure out a way to factor pi out and represent it.

        if self._spherical_repr:

            pretty_theta = where_is_pi(self.theta)
            pretty_phi = where_is_pi(self.phi)

            return f'({self.rho}, {pretty_theta}, {pretty_phi})'

        return str((self.x, self.y, self.z))


def angle(a: 'Vector3', b: 'Vector3', degree: bool = False) -> RealNumber:

    if degree:

        return a.angle(b, degree=True)

    return a.angle(b)


if __name__ == '__main__':

    a = [1, 2, 3]
    v1 = Vector3(*a)
    v2 = Vector3(1, 3, 2)

    print((1, 2) > Vector3(1, 2, 3))
