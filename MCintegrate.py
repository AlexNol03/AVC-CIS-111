# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:34:45 2023

@author: Alex Nolan
"""

def MCint(f, a, b, n):
    """

    Parameters
    ----------
    f : TYPE function
        DESCRIPTION.
    a : TYPE float
        DESCRIPTION. lower limit
    b : TYPE float
        DESCRIPTION. upper limit
    n : TYPE int
        DESCRIPTION.

    Returns
    -------
    integral of f from a to b

    """
    from random import random
    
    maxF = .5
    
    area = 0
    saveX = []
    saveY = []
    
    for i in range(n):
        
        #x between a and b
        #z between 0 and maxF
        
        randNoX = random()*(b-a)+ a
        randNoY = random()*maxF
        saveX.append(randNoX)
        saveY.append(randNoY)
        
        if randNoY <= f(randNoX): area += 1
        
    boxArea = (b-a)*maxF
    integral =  area/n * boxArea
    print(min(saveX), max(saveX))
    print(min(saveY), max(saveY))
    return(integral)

if __name__ == "__main__":
    
    #import numpy as np
    #import matplotlib.pyplot as plt
    
    def f(x) :
        return x**2
    
    area = MCint(f, 0.5, 2., 500000)
    
    print(round(area,2))
    print(f"integ = {area: 0.2f}")