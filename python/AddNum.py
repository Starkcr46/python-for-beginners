#Program for adding two numbers
#Created on : 04-April-2025
#Created by : Chris Stark

print('This is a program to add two numbers')
try : 
    x = input('Key in the first number : ')
    y = input('Key in the second number: ')
    x = int(x)
    y = int(y)
except :
    print('Alert : input only the integers')
else :
    z = x + y
    print('The value of Sum : ', z)
