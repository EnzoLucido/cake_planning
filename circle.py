import numpy as np

def area(radius):
    return (radius**2) * np.pi

def total_area(radius_list):
    total = 0
    for radius in radius_list:
        total += area(radius)
    return total
