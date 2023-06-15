# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:50:25 2023

@author: Alex nolan
"""

def calculate_max_height(initial_velocity):
    # Acceleration due to gravity
    acceleration = -32.17  # feet per second squared

    # Time taken to reach maximum height
    time = -initial_velocity / acceleration

    # Maximum height reached
    max_height = initial_velocity * time + 0.5 * acceleration * time ** 2

    return max_height

initial_velocity = 50  # feet per second
max_height = calculate_max_height(initial_velocity)
print("Maximum height reached:", max_height, "feet")
