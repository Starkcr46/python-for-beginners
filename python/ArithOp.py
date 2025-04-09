#Arithmetic operators
#Created on: 05-April-2025
#Created By: Chris Stark

print('This program demonstrates the various arithmentic operations using integers')
try :
    integerOne = int(input('input int #1 :'))
    integerTwo = int(input('input int #2 :'))

except :
    print('Error: inputs must be integers')

else :
    add = integerOne + integerTwo
    sub = integerOne - integerTwo
    mult = integerOne * integerTwo
    div = float(integerOne / integerTwo)
    mod = integerOne % integerTwo
    floor = integerOne // integerTwo
    exp = integerOne ** integerTwo
    print('Addition :', add)
    print('Subtraction :', sub)
    print('Multiply :', mult)
    print('Divide :', div)
    print('Modulus :', mod)
    print('Floor Division :', floor)
    print('Exponent :', exp)
