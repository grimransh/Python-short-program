# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:17:38 2024

@author: ANURAG PAL
"""

""" Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist."""

def listt(nums):
    try:
        r = len(nums)
        print("Length of the list:", r)
    except AttributeError:
        print("Error: The list does not have a 'length' attribute.")

nums = list(map(int,input("enter the list with spaces: ").split()))

listt(nums)
