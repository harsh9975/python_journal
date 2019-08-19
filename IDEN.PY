# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 12:00:32 2018

@author: Administrator
"""
n=int(input("enter the order of the matrix"))
for x in range(0,n): 
    for y in range(0,n):
         if (x==y):
                print(1,end=" ")
         else:
                print(0,end=" ")
    print()
    
