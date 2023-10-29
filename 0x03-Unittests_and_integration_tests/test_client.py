#!/usr/bin/env python3
"""This module contains unittests for clients.py
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """This class tests the gihub org client using mocks for gihub api"""

    @parameterized.expand([
        ('google', {'login': 'google', 'id': 1, 'repos_url': 'google.com'}),
        ('abc',  {'login': 'abc', 'id': 1, 'repos_url': 'abc.com'})
    ])
    @patch.object(GithubOrgClient, 'org')
    def test_org(self, input, expected, mock_org):
        """tests an organization's github api info"""
        mock_org.return_value = expected
        self.assertEqual(GithubOrgClient.org(), expected)

    

if __name__ == '__main__':
    unittest.main()