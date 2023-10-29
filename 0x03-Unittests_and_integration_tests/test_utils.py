#!/usr/bin/env python3
"""
This module contains unit tests for the
    access_nested_map function in the utils module.
"""
import unittest
from unittest import mock
from parameterized import parameterized, parameterized_class
import utils
from utils import memoize
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
            mock_get.return_value.json.return_value = expected
            self.assertEqual(utils.get_json(url), expected)
            mock_get.assert_called_with(url)


class TestMemoize(unittest.TestCase):
    """tests memoize cache """
    def test_memoize(self):
        """Test memoize caching"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        test_instance = TestClass()
        with mock.patch.object(test_instance, 'a_method') as mock_method:
            mock_method.return_value = 45
            call_1 = test_instance.a_property
            call_2 = test_instance.a_property

            mock_method.assert_called_once()
            self.assertEqual(call_1, 45)
            self.assertEqual(call_2, 45)


if __name__ == '__main__':
    unittest.main()
