#Factorial with recurstion
#Created on: 08-April-2025
#Created By: Chris Stark

print('This program calculates factorial with recursion')

def factorial(num) :
    if(num < 1):
      return 'Only positive ints allowed'
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)
        

intMax = int(input('input factorial value :') or 1)

print('result :', factorial(intMax))



