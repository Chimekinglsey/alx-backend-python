#!/usr/bin/env python3
"""
This module contains unit tests for the
    access_nested_map function in the utils module.
"""
import unittest
from unittest import mock
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

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map: Mapping,
                               path: Sequence, expected: int) -> None:
        """ Test the access_nested_map function """
        self.assertEqual(utils.access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, map: Mapping, path: Sequence,
                                         expected: KeyError) -> None:
        """ Test the access_nested_map function """
        self.assertRaises(expected, utils.access_nested_map, map, path)


class TestGetJson(unittest.TestCase):
    """Test utils.get_json() mock object """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, expected):
        """create mock for utils.get_json() """
        with mock.patch("utils.requests.get") as mock_get:
            mock_response = mock.MagicMock()
            mock_response.json.return_value = expected
            mock_get.return_value = mock_response

            result = utils.get_json(url)
            mock_get.assert_called_with(url)
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
