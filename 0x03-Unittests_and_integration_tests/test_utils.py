#!/usr/bin/env python3
"""
This module contains unit tests for the
access_nested_map function in the utils module.
"""
import unittest
from parameterized import parameterized
import utils
from typing import (
    Mapping,  # Type hint for a mapping type.
    Sequence,  # Type hint for a sequence type.
    Any,  # Type hint for any data type.
)


class TestAccessNestedMap(unittest.TestCase):
    """Test class for AccessNestedMap"""

    @parameterized.expand([
        ("depth_1_1", {"a": 1}, ("a",), 1),  # Test case 1
        ("depth_2_1", {"a": {"b": 2}}, ("a",), {'b': 2}),  # Test case 2
        ("depth_2_2", {"a": {"b": 2}}, ("a", "b"), 2),  # Test case 3
    ])
    def test_access_nested_map(self, name: str, map: Mapping[str, Any],
                               path: Sequence, expected: int) -> None:
        """
        Test the access_nested_map function.

        Args:
            name (str): A descriptive name for the test case.
            map (Mapping[str, Any]): A mapping or nested map to test.
            path (Sequence): A sequence representing the
                path to access a value in the map.
            expected (int): The expected result when accessing the nested map.

        Returns:
            None
        """
        self.assertEqual(utils.access_nested_map(map, path), expected)


if __name__ == '__main__':
    unittest.main()
