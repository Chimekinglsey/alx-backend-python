#!/usr/bin/env python3
"""
This module contains unit tests for the
    access_nested_map function in the utils module.
"""
import unittest
from parameterized import parameterized, parameterized_class
import utils
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test class for AccessNestedMap"""
    # def setUp(self) -> None:
    #     self.nested_map = utils.access_nested_map()

    @parameterized.expand([
        ("depth_1_1", {"a": 1}, ("a",), 1),
        ("depth_2_1", {"a": {"b": 2}}, ("a",), {'b': 2}),
        ("depth_2_2", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, name: str, map: Mapping[str, Any],
                               path: Sequence, expected: Any) -> None:
        """ Test the access_nested_map function """
        self.assertEqual(utils.access_nested_map(map, path), expected)


if __name__ == '__main__':
    unittest.main()
