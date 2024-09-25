# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:02:58 2024

@author: ANURAG PAL
"""

""" python program to calculate factorial gamma of number"""

import math

def fact(number):
    if number==1 or number==0:
        return 1
    else:
        return(number*fact(number-1))

num1=int(input("Enter the number: "))
print("Factorial of",num1,"is :",fact(num1))
print("Factorial of",num1,"is using math :",math.factorial(num1))

num2=float(input("Enter the number: "))
print("Factorial of",num2,"is using math :",math.gamma(num2))