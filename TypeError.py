# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:59:41 2024

@author: ANURAG PAL
"""

""" Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical."""

def num_in(string):
    while True:
        try:
            value = float(input(string))
            return value
        except ValueError:
            print("Error: Invalid input. Please Input a valid number.")

n1 = num_in("Input the first number: ")
n2 = num_in("Input the second number: ")

result = n1 * n2

print("Product of the said two numbers:", result)
