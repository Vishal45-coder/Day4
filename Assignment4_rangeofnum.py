# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:59:30 2020

@author: vishal
"""


X = 1000
Y = 7000

def checkRange(num):
   # using comaparision operator
   if (a>X and a<Y):
       print(f"{a} is in between ({X} {Y})")
   else:
      print(f"The number {a} is not in range ({X}, {Y})")

# Test Input
a=int(input(("Enter the number you want to search")))
checkRange(a)

