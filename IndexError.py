# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:03:13 2024

@author: ANURAG PAL
"""

""" Python program that executes an operation on a list and handles an IndexError exception if the index is out of range."""

def test_index(data, index):
    try:
        print("Result:",data[index] )
    except IndexError:
        print("Error: Index out of range.")

nums = list(map(int,input("enter the list with spaces : ").split()))

index = int(input("Input the index: "))

test_index(nums, index)
