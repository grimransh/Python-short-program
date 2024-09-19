# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:35:23 2024

@author: ANURAG PAL
"""

""""Python program to find square root of a number without importing math module"""
num = int(input("Enter the positive number:\n"))
trial=num/2
error=0.000001
while abs(trial*trial-num)>error:
    trial=(trial+num/trial)/2               # Newton-Raphson Method
print("Square root of",num,"is:\n",trial)