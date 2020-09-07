from vector3 import Vector3, Spherical, Cylindrical, Polar, MagAngle, angle
from math import pi

a = Vector3(0, 0, 1)
b = Vector3(1, 0, 2)

F = MagAngle(10)
d = MagAngle(100)

i = Vector3(1, 0, 0)
j = Vector3(0, 1, 0)
k = Vector3(0, 0, 1)

# print(f'i x j = ', end='')
# (i ** j).pprint()
# print(f'i x k = ', end='')
# (i ** k).pprint()
# print(f'j x k = ', end='')
# (j ** k).pprint()

# Vector3(1, 1, 1).pprint()

# print(Spherical(1, pi, 2 / 3 * pi))

print(Vector3(1, 1, 1).to_cylindrical())