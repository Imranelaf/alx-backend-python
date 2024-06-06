#!/usr/bin/env python3

'''
Type-annotated function sum_list that takes a list input_list of floats as
argument and returns their sum as a float.
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Returns the sum of a list of floats

    Parameters:
        input_list : list[float]

    Returns:
        float: sum of input_list
    '''
    return sum(input_list)
