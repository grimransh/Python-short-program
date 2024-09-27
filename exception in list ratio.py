# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:36:52 2024

@author: ANURAG PAL
"""

""" Program to input two same size list and find the ratio of same index"""

def listinput(l,r):
    for i in range(r):
        num=float(input("Enter number: "))
        l.append(num)
    return l

def getRatio(l1,l2,r):
    list3=[]
    for i in range(r):
        try:
            ratio = list1[i]/list2[i]
            list3.append(ratio)
        except Exception:
            list3.append('NAN')
    return(list3)

length=int(input("enter the length of list: "))

print("list 1")
list1=[]
listinput(list1, length)

print("list 2")
list2=[]
listinput(list2, length)

temp=getRatio(list1,list2,length)
print(temp)