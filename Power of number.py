# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:41:36 2024

@author: ANURAG PAL
"""

"""program to calculate power of number"""

def power_using_loop(num, power):
    result=1
    for i in range(power):
        result *=num
    return result

def power_uaing_recursion(num,power):
    if power==0:
        return 1
    if power>=1:
        return num*power_uaing_recursion(num, power-1)

number=int(input("Enter the number: "))
power=int(input("Enter the positive integer power: "))

res1=power_using_loop(number, power)
print("Result using loop: ",res1)

res2=power_uaing_recursion(number, power)
print("Result using recursion: ",res2)