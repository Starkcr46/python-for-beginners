'''Module for volume calculation'''
pi = 3.14

def VolumeOfSphere(r) :
    rCubed = r ** 3
    dec = 4 / 3
    return dec * pi * rCubed

def VolumeOfCube(s) :
    return s ** 3

def VolumeOfCylinder(r, h) :
    rSquared = r ** 2
    return pi * rSquared * h

def VolumeOfRectangularPrism(l, w, h) :
    return l * w * h

def VolumeOfPyramid(l, w, h) :
    vol = l * w * h
    return vol / 3

def VolumeOfCone(r, h) :
    height = h / 3
    rSquared = r ** 2
    return pi * rSquared * height
