# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 17:41:03 2023

@author: Alex Nolan
"""

def computesPmt(PV, r, n):
    """

    Parameters
    ----------
    PV : TYPE float
        DESCRIPTION.
    r : TYPE float
        DESCRIPTION.
    n : TYPE integer
        DESCRIPTION.

    Returns
    -------
    Pmt : TYPE float
        DESCRIPTION. amt paid per month

    """
    
    Pmt = r * PV/(1-(1+r)**-n)
    return Pmt

def computesPV(Pmt, r, n):
    """
    

    Parameters
    ----------
    Pmt : TYPE float
        DESCRIPTION. how much I can afford for monthly payment
    r : TYPE float
        DESCRIPTION.interest rate APR
    n : TYPE integer
        DESCRIPTION. number of months

    Returns
    -------
    PV: Type float
        DESCRIPTION. amount of $$ I can afford to borrow
    PV = (1-(1+r)**(-n) *Pmt/r

    """
    
    r = r/100 # convert APR to decmial
    r = r/12
    
    PV = (1-(1+r)**(-n)) * Pmt / r
    return PV

# input the PV
import numpy as np

while(True):
    choice = int(input('enter choice 1 for PV, 2 for Pmt   -> '))
    if (choice == 1 or choice == 2):
        break
    else:
        print(f"enter a 1 or a 2, your entered {choice}")

if choice == 2:
    PV = input('enter PV: ')
    PV = float(PV)
    print(f"PV = {PV} \n")
    
    r = input('interest APR: ')
    r = float(r)/100
    r = r/12
    print(f"interest = {r: 0.3f} \n")
    
    n = int(input('how many months: '))
    print(f"\nn = {n} months \n")
    
    Pmt =  computesPmt(PV, r, n)
    Pmt = np.round(Pmt, 2)
    print(f"payment is ${Pmt: } per month")
    
    
if choice == 1:
    
    n = int(input('no of months: '))
    print(f"\nn = {n} months \n")
    
    r = input('interest APR: ')
    r = float(r)/100
    r = r/12
    print(f"interest = {r: 0.3f} \n")
    
    Pmt = input('enter Pmt: ')
    Pmt = float(Pmt)
    print(f"Pmt - {Pmt} \n")
    
    PV = computesPV(Pmt, r, n)
    print (PV)

PV =  computesPV(85.61, 5, 12 )
print(PV)




