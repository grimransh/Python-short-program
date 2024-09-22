# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:50:56 2024

@author: ANURAG PAL
"""

"""program to print pyramid
        *

      * * *

    * * * * *

  * * * * * * *
"""

x=int(input("Enter the number of rows\n"))
for i in range(1,x+1):
    for j in range(x-i):
        print("  ",end="")

    for k in range(2*i-1):
        print("* ",end="")
    print("\n")