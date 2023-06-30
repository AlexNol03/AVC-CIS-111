# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 17:25:05 2023

@author: be
"""

def split_dollar(amount, denominations):
    # Base case: if the amount is zero, there is one valid split (no coins)
    if amount == 0:
        return 1

    # Base case: if the amount is negative or there are no denominations, return 0
    if amount < 0 or len(denominations) == 0:
        return 0

    # Recursive case: split the amount using the first denomination and
    # recursively split the remaining amount using all denominations
    return split_dollar(amount - denominations[0], denominations) + \
           split_dollar(amount, denominations[1:])


# Test the function
denominations = [1, 5, 10, 25, 50]
amount_to_split = 100  # $1.00
ways_to_split = split_dollar(amount_to_split, denominations)
print(f"Number of ways to split ${amount_to_split / 100:.2f}: {ways_to_split}")