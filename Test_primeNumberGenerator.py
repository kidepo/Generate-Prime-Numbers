# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 04:54:36 2017

@author: Paul
"""

"""Unit tests for prime_numbers module."""

import unittest
import primeNumbersGenerator


class TestPrimeGenerator(unittest.TestCase):




    def test_zero(self):
        """Testing if zero is correctly determined not to be prime."""

        self.assertEqual(generatePrimeNumbers(0), "Zero or One cannot be prime numbers.")
        
    def test_fifty(self):
        """Testing if prime numbers are correctly generated."""
        
        self.assertEqual(prime_numbers(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

    def test_one(self):
        """"Testing if one is correctly determined not to be prime."""

        self.assertEqual(generatePrimeNumbers(1), "Zero or One cannot be prime numbers.")

    def test_string(self):
        """Testing if error returned if a string is entered."""

        self.assertEqual(generatePrimeNumbers("String"), "Only integers are allowed.")

    def test_invalid_type_string_list(self):
        """Testing if error returned if input not integer."""

        self.assertEqual(generatePrimeNumbers([]), "Only integers are allowed.")

    def test_only_positive(self):
        """Testing if error returned if negative integers input."""

        self.assertEqual(generatePrimeNumbers(-7), "Not possible to generate prime numbers for integers less than 2.")


if __name__ == "__main__":
    unittest.main()
