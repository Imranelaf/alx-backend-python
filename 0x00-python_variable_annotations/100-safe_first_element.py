#!/usr/bin/env python3

'''
Type-annotated function safe_first_element that takes a sequence lst as input
and returns the first element of the sequence if it exists, otherwise None.
'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Return the first element of a sequence if it exists, otherwise return None.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the input sequence if it exists,
        otherwise None.
    '''
    if lst:
        return lst[0]
    else:
        return None
