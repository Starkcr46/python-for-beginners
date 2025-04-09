#Find prime numbers between 1 and input value
#Created on: 05-April-2025
#Created By: Chris Stark

print('This program finds primes between 1 and input value')

def isPrime(num) :
    subRng = range(2, num - 1)
    for j in subRng:
        if(num % j == 0):
            return False

    else:
            return  True

intMax = int(input('input upper limit :') or 1)

rng = range(1, intMax)

for i in rng:
    if(isPrime(i) and i != 1):
        print(i)




