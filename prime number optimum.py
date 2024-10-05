# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:08:09 2024

@author: ANURAG PAL
"""

""" Program to Get the key of the minimum value in a dictionary"""

num = int(input("Enter the POSITIVE number: "))


if num==0 or num==1:
    print(num," is neither a prime nor a composite number.")
else:
    is_prime = True

    for i in range(2,num-1):
        if num%i == 0:
            is_prime = False
    if is_prime:
        print(num," is prime number")
    else:
        print(num," is composite number")