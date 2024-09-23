# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:57:49 2024

@author: ANURAG PAL
"""

"""Program to print right angle traingle"""
"""
*
**
***
****
*****
"""
a=int (input("Enter the number of rows: "))
for i in range(1,a+1):
    for j in range(i):
        print("*",end="")
    print()

"""
    *
   **
  ***
 ****
*****
"""

b=int (input("Enter the number of rows: "))
for i in range(1,b+1):
    for j in range(b-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()