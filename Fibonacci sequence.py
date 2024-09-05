# -*- coding: utf-8 -*-
"""
Fibonacci sequence
"""
print("This program id print fibonacci sequence");
n=int(input('enter the number: '));
a,b,t=0,1,n-2;

print(a,b, end =" ");
for i in range(t):
    s=a+b;
    print(s, end =" ");
    a=b;
    b=s;
