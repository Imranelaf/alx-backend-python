#!/usr/bin/env python3

'''
This function takes a list of integers and floats and returns the sum of all
the numbers in the list.
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    This function takes a list of integers and floats and returns the sum of
    all the numbers in the list.

    Parameters:
        mxd_lst : list[int] or list[float]

    Returns:
        float: sum of mxd_lst
    '''
    return sum(mxd_lst)
