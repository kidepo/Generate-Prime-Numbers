# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 04:10:22 2017

@author: Paul
"""

def generatePrimeNumbers(upper):
    primeNumbers =[]
    # Python program to display all the prime numbers within an interval
    if upper in (0, 1):
        return "Zero or One cannot be prime numbers."
    
    if upper < 2:
        return "Not possible to generate prime numbers for integers less than 2."
    
    if type(upper) != int:
            return "Only integers are allowed."
    lower = 0

    for num in range(lower,upper + 1):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               primeNumbers.append(num)
    return primeNumbers
