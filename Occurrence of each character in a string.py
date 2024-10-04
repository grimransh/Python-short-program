# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:48:39 2024

@author: ANURAG PAL
"""

""" Program to Count the occurrence of each character in a string"""

string = input("Enter the string : ")
times = {}
for char in string :
    if char in times:
        times[char] += 1
    else:
        times[char] = 1

print("occurance of each character: \n",times)