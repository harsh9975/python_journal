# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:05:43 2018

@author: Administrator
"""

from numpy import linalg
 
A=[[2,-1,5,1],[3,2,2,-6],[1,3,3,-1],[5,-2,-3,3]]
B=[-3,-32,-47,49]
C=[[2,-1,5,1],[3,2,2,-6],[1,3,3,-1],[5,-2,-3,3]]
X=[]
for i in range(0,len(B)):
    for j in range(0,len(B)):
        C[j][i]=B[j]
        if i>0:
            C[j][i-1]=A[j][i-1]
    X.append(round(linalg.det(C)/linalg.det(A),1))
 
print('w=%s'%X[0],'x=%s'%X[1],'y=%s'%X[2],'z=%s'%X[3])
 