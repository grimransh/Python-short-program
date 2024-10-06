# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:01:29 2024

@author: ANURAG PAL
"""

""" Program to Merge two dictionaries"""

dict1 = {'t': 1, 'h': 1, 'i': 2, 's': 2, ' ': 4, 'a': 4}
dict2 = {'a': 4, 'n': 2, 'u': 2, 'r': 2, 'g': 2, '5': 5}

merge_dict = {**dict1, **dict2}

print("mearged dictionary : ",merge_dict)