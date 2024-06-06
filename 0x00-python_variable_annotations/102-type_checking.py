#!/usr/bin/env python3

'''
Type-annotated function zoom_array that takes a tuple lst of integers and an
optional integer factor that defaults to 2. The function returns a list of
integers that is the result of repeating each element in lst by factor times.
'''

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Zooms in on the input sequence by repeating each element by the specified
    factor.

    Args:
        lst (Tuple): A sequence of elements.
        factor (int): The number of times each element in the input sequence
                      should be repeated. Defaults to 2.

    Returns:
        List: A list containing elements of the input sequence repeated by the
              specified factor.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
