#!/usr/bin/env python3

'''
This module contains the test for the utils module
'''
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict, Any, Tuple
import unittest
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    '''
    This class is for testing access_nested_map
    '''
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        '''
        This method is for testing access_nested_map
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str]
    ) -> None:
        '''
        This method is for testing access_nested_map with exception
        '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
