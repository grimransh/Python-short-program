# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:12:39 2024

@author: ANURAG PAL
"""

"""  Python program to calculate the length of a string."""

def string_length(strr):
    count = 0
    for char in strr:
        count += 1
    return count
strr = input("enter the string: ")
print(string_length('w3resource.com')) 
