# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 04:10:22 2017

@author: Paul
"""



def primetest(potentialprime):
    divisor = 2
    while divisor <= potentialprime:
        if potentialprime == 2:
            return True
        elif potentialprime % divisor == 0:
            return False
            break
        while potentialprime % divisor != 0:
            if potentialprime - divisor > 1:
                divisor += 1
            else:
                return True


def generatePrimeNumbers(numprimes):
    count = 0
    potentialprime = 2
    primeNumbers = []
    
    if numprimes in (0, 1):
        return "Zero or One cannot be prime numbers."
    
    if numprimes < 2:
        return "Not possible to generate prime numbers for integers less than 2."
    
    if type(numprimes) != int:
            return "Only integers are allowed."
            
    while count < int(numprimes):
        if primetest(potentialprime) == True:
            primeNumbers.append(potentialprime)
            count += 1
            potentialprime += 1
        else:
            potentialprime += 1
    return primeNumbers  