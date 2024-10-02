# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:01:54 2024

@author: ANURAG PAL
"""

""" Program to check if a number is a palindrome"""

def palindrome(a):
    if a == a[::-1]:
        print(a," is palindrome")
    else:
        print(a," is NOT palindrome")

a = input("enter the string or number")
palindrome(a)