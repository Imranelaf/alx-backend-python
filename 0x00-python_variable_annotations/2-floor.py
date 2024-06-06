#!/usr/bin/env python3

'''
Type-annotated function floor that takes a float n as argument and returns the
floor of the float.
'''

import math


def floor(n: float) -> int:
    '''
    Returns the floor of a float

    Parameters:
        n : float

    Returns:
        int: floor of n
    '''
    return math.floor(n)
