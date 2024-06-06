#!/usr/bin/env python3

'''
This function takes a string and a number and returns a tuple containing the
string and the number squared.
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    This function takes a string and a number and returns a tuple containing
    the string and the number squared.

    Parameters:
        k : str
        v : int or float

    Returns:
        tuple[str, float]: a tuple containing the string and the number squared
    '''
    return (k, v ** 2.0)
