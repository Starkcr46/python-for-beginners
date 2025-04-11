#Arithmetic operators
#Created on: 05-April-2025
#Created By: Chris Stark

print('This program demonstrates the various arithmentic operations using integers')

def addNum(int1, int2):
    return int1 + int2
def subNum(int1, int2):
    return int1 - int2
def multNum(int1, int2):
    return int1 * int2
def divNum(int1, int2):
    return int1 / int2
def modNum(int1, int2):
    return int1 % int2
def floorNum(int1, int2):
    return int1 // int2
def expNum(int1, int2):
    return int1 ** int2

try :
    integerOne = int(input('input int #1 :'))
    integerTwo = int(input('input int #2 :'))

except :
    print('Error: inputs must be integers')

else :
    add = addNum(integerOne, integerTwo)
    sub = subNum(integerOne, integerTwo)
    mult = multNum(integerOne, integerTwo)
    div = divNum(integerOne, integerTwo)
    mod = modNum(integerOne, integerTwo)
    floor = floorNum(integerOne, integerTwo)
    exp = expNum(integerOne, integerTwo)
    print('Addition :', add)
    print('Subtraction :', sub)
    print('Multiply :', mult)
    print('Divide :', div)
    print('Modulus :', mod)
    print('Floor Division :', floor)
    print('Exponent :', exp)


