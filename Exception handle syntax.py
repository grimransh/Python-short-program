# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
""" Python"""

""" exception handle syntax"""

def div(x,y):
    try:
        result = float(x)/float(y)
    except ZeroDivisionError:
        print("denominator can't be zero")
    except Exception:
        print("something went wrong")
    else:
        print("Answer is ",result)
    finally:
        print("\033[5;30;46m code successfully executed \033[0m")
# \033[ this is same for exection
# 1 for style of text 1 for bold
# 34 for text color 34 for blue
# 46m for background color 46m for cyan
x =input("enter the numerator : ")
y =input("enter the denominator : ")

a= div(x,y)

print(a)