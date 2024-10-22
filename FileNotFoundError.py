# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:49:59 2024

@author: ANURAG PAL
"""
"""  Python program that opens a file and handles a FileNotFoundError exception if the file does not exist."""

def open_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:",contents)
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")

filen = input("Input a file name: ")

open_file(filen) 
