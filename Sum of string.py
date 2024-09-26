# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:37:32 2024

@author: ANURAG PAL
"""
""" Program to calculate sum of number in the estring"""

def sums(s1):
    r=len(s1)
    s=0
    for i in range(r):
        try:
            s +=int(s1[i])
        except Exception:
            s=s+0
    return s

string=input("Enter the string:\n")

temp=sums(string)
print(temp)