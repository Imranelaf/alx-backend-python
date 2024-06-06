#!/usr/bin/env python3

'''
This module contains a function that returns a function that multiplies a float
by a given multiplier.
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float as input and
                                  returns the result of multiplying it by the
                                  multiplier.
    """
    def multiplier_func(x: float) -> float:
        """
        Multiply a float by the given multiplier.

        Args:
            x (float): The input float.

        Returns:
            float: The result of multiplying the input float by the multiplier.
        """
        return x * multiplier

    return multiplier_func
