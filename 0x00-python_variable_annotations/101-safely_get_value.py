#!/usr/bin/env python3

'''
Type-annotated function safely_get_value that takes a Mapping dct, Any key, and
an optional Union[T, None] default argument and returns the value associated
with key in dct if it exists, otherwise default.
'''

from typing import TypeVar, Mapping, Optional, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    '''
    Return the value associated with the key in the input dictionary if it
    exists, otherwise return the default value.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to search for in the input dictionary.
        default (Union[T, None]): The default value to return if the key is not
        found in the input dictionary. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key in the input
        dictionary if it exists, otherwise the default value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
