# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 17:18:38 2023

@author: Alex Nolan

"""

import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([3,5,7,9,11])

sumX = 0
sumX2 = 0
sumXY = 0
sumY = 0

n = len(x)
for i in range (5):
    sumX += x[i]
    sumY += y[i]
    sumX2 += x[i]**2
    sumXY += x[i]*y[i]
    
a = (sumY*sumX2-sumX*sumXY)/(n*sumX2-sumX**2)
b =(n*sumXY-sumX*sumY)/(n*sumX2-sumX**2)
    
print(a,b)
    
yHat = []
for i in range(n):
    yHat.append(b*x[i] + a)
    
    print(y, yHat)