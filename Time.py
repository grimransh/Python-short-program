# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:05:53 2024

@author: ANURAG PAL
"""

""" TIME """

import time

# prints the number of ticks spent since 12 AM, 1st January 1970  
print ("seconds from 12 AM, 1st January 1970 :\n",time.time())

print("\n")

# returns a time tuple
print(time.localtime(time.time()))

info = """
index of tupple
0       Year                4 digit 
1       Month               1 to 12
2       Day                 1 to 31
3       Hour                0 to 23
4       Minute              0 to 59
5       Second              0 to 60
6       Day of weak         0 to 6
7       Day of year         1 to 366
8       Daylight savings    -1, 0, 1 , or -1

"""
print(info)

print("\n")

# returns the formatted time      
print(time.asctime(time.localtime(time.time())))  

print("\n")

#Each element will be printed after 1 second
for u in range(5):
    print (u)
    time.sleep(1)
    
print("\n")
