# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:29:15 2024

@author: ANURAG PAL
"""

""" Program to largest in list"""

my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

largest = max(my_list)
print("Largest number in list using keyword: ",largest)

large=my_list[0]
for num in my_list:
    if num>large:
        large=num
print("Largest number in list using loop: ",large)