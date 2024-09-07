# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 23:01:45 2024

@author: ANURAG PAL
"""
"""Python Program to Swap Two Elements in a List"""

print("Python Program to Swap Two Elements in a List")
my_list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("the list is : \n",my_list)

pos1=int(input("enter the position you want to change: "))-1
pos2=int(input("enter the position fron you want to change: "))-1

my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]

print("List after swapping:", my_list)