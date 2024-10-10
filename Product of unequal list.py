# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:40:59 2024

@author: ANURAG PAL
"""

def prod(list1,list2):
    list3 = []
    l1=len(list1)
    l2=len(list2)

    for i in range(max(l1,l2)):
        if l1>l2:
            try:
                xx=list1[i]*list2[i]
                list3.append(xx)
            except Exception:
                list3.append(list1[i])
        else:
            try:
                yy=list1[i]*list2[i]
                list3.append(yy)
            except Exception:
                list3.append(list2[i])

    return list3

listA = list(map(int,input("Enter the list1 with space:\n").split()))
listB = list(map(int,input("Enter the list2 with space:\n").split()))

output =prod(listA, listB)

print("Product of list is:\n",output)