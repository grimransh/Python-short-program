# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:24:54 2024

@author: ANURAG PAL
"""

""" Python program to add two file in alternate files"""
with  open('trial1_for adding.txt','r') as file1, open('trial2_for adding.txt','r') as file2, open('output_alternate_add.txt','w') as output:
    content1=file1.readlines()
    content2=file2.readlines()

    max_length= max(len(content1),len(content2))

    for i in range(max_length):
        if i<len(content1):
            output.write(content1[i])
        if i<len(content2):
            output.write(content2[i])

with open('output_alternate_add.txt','r') as output:
        print(output.read())