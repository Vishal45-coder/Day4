# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:11:10 2020

@author: vishal
"""


a=int(input("enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
if(a>b and a>c):
    print(f"a={a} is greater ")
elif(b>c and b>a):
    print(f"b={b} is greater")
elif(c>a and c>b):
    print(f"c={c} is greater")
else:
    print("All are equal")    