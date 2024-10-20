# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:07:50 2024

@author: ANURAG PAL
"""

""" Python program to convert Year/Month/Day to Day of Year """

import datetime

today = datetime.datetime.now()
first_day =datetime.datetime(today.year, 1, 1)

day_of_year = (today - first_day).days + 1

print(day_of_year)
