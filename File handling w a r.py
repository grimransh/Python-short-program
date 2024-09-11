# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:29:26 2024

@author: ANURAG PAL
"""

""" Python program to create new text file"""

var=open("trial.txt","w")                       #creating file or replacing file
var.write("This is first line. ")                #writing content
var.write("This is continuation of first line. ")
var.close()                                     #closing file

""" Python program to appending text to file"""
var=open("trial.txt","a")
var.write("This is appending first line.\n")
var.close()

""" python program to append multiple line"""

var=open("trial.txt","a")

lines=[
        "1: Two roads diverged in a yellow wood, \n",
        "2: And sorry I could not travel both \n",
        "3: And be one traveler, long I stood \n",
        "4: And looked down one as far as I could \n",
        "5: To where it bent in the undergrowth; \n",
]

for line in lines:
    var.write(line)
var.close()

"""program to print previous file"""
var=open("trial.txt","r")
output=var.read()
print(output)

var.close()