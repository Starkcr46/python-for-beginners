#Program to calculate various volumes of shapes/demonstrating module import

import sys
sys.path.append('c:\\python-for-beginners\\python')
import Volume

r = int(input('What is the radius of the shape?'))
l = int(input('What is the length of the shape?'))
w = int(input('What is the width of the shape?'))
h = int(input('What is the height of the shape?'))

print('Volume of Sphere :', Volume.VolumeOfSphere(r))
print('Volume of Cube :', Volume.VolumeOfCube(l))
print('Volume of Cylinder :', Volume.VolumeOfCylinder(r, h))
print('Volume of Rectangular Prism :', Volume.VolumeOfRectangularPrism(l, w, h))
print('Volume of Pyramid :', Volume.VolumeOfPyramid(l, w, h))
print('Volume of Cone :', Volume.VolumeOfCone(r, h))

