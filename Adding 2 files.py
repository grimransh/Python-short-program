# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:06:17 2024

@author: ANURAG PAL
"""

""" program to add 2 text file in new file and them print them"""

with open("trial1_for adding.txt","r") as file1:        #file containing half of the lyrics
    content1=file1.read()

with open("trial2_for adding.txt","r") as file2:        #file containing half of the lyrics
    content2=file2.read()

with open('output_add.txt', 'w') as output:             # created file containing all combind lrics
    output.write(content1)
    output.write(content2)

with open("output_add.txt","r") as out:
    output_print=out.read()
    print(output_print)