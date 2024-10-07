# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:17:36 2024

@author: ANURAG PAL
"""

""" Program to delete duplicate from list"""

my_list=[1,1,2,2,3,3,4,4,5,5,'A','A','b','c']

new_order_list = list(set(my_list))
print("new list without duplicate: ",new_order_list)

new_list = list(dict.fromkeys(my_list))
print('new list without duplicate with same order: ',new_list)