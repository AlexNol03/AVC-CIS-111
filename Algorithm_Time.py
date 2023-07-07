# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 17:15:43 2023

@author: Alex Nolan
"""

import numpy as np
import matplotlib.pyplot as plt

## define a function that computes the n+1
# the previous two fibonnacci

def aliens (F, n): 
    """
    

    Parameters
    ----------
    F : TYPE float array
        DESCRIPTION. F[n] is the n-th Fibonacci number
    n : TYPE integer
        DESCRIPTION. index into F

    Returns
    -------
    TYPE
       F[n+1], the (n+1)-st Fibonacci number

    """
    
    F[n] = F[n-1] + F[n-2]
    return F[n]
def aliens2(F,n):
    """
    

    Parameters
    ----------
    F : TYPE float list
        DESCRIPTION.
    n : TYPE integer
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    if len(F) < 2:
        print(' F is not long enough')
        return(0)
    
    F.append[F[n-1] + F[n-2]]
    return F

if __name__ == "__main__":
    
    ## first use an array
    
    F = np.zeros(100)
    F[0] = 0
    F[1] = 1
    
    for n in range(2, 20):
        F[n] = aliens(F, n)

    intF = [int(x) for x in F[:20]]
    print(intF)
    ## now use a list
    
    F = intF
    d = []
    
    for n in range(2,19):
        d.append(F[n]/F[n-1])
        
        print (d)
        
        ## to finish this, comput d[n] = F[n+1]/F[n] for n = 1, 2, ... 20
        
        d = F
        plt.plot(d,'.')
        
        

