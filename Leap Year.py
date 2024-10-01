# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:03:56 2024

@author: ANURAG PAL
"""

"""Program to cheack year is leap or not"""

def leap(y):
    if (y%4==0 and y%100!=0) or (y%400==0):
        print(y," is leap year ")
    else:
        print(y," is not leap year")


year = int(input("enter the year: "))
leap(year)