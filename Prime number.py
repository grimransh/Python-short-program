# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""
"""program to check if number is prime or not"""
def prime(x):
    t=0
    for i in range(2,x):
        if x%i==0:
            t+=1
    return t

num=int(input("enter any number: " ))

temp=prime(num)

if temp==0 and num>1:
    print(num," is prime number");
else:
    print(num," is not prime number");