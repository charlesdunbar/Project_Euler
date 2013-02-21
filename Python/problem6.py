'''
Created on Nov 23, 2010

@author: Charles

Problem 6:
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares 
of the first ten natural numbers and the square of 
the sum is 3025  385 = 2640.

Find the difference between the sum of the squares 
of the first one hundred natural numbers and the square of the sum.
'''

def sumOfSquares(num):
    retval = 0
    for x in range(1,num+1): #Need num+1 since range doesn't include last number
        retval += x**2
    return retval

def squareOfSums(num):
    return (sum(range(1,num+1)))**2

def diffSums(square, sum):
    return squareOfSums(square) - sumOfSquares(sum) 

print(squareOfSums(10))
print(sumOfSquares(10))
print(diffSums(100,100))
    
