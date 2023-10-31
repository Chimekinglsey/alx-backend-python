#!/usr/bin/env python3
"""This module contains unittests for clients.py
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """test for public_repo url """
        obj = GithubOrgClient('abc')
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            payload = {"payload": True, "repos_url": "success"}
            mock_org.return_value = payload
            self.assertEqual(obj._public_repos_url, 'success')

    @patch.object(GithubOrgClient, 'org')
    def test_public_repos(self, mock_json):
        """unit-test for GithubOrgClient.public_repos."""
        value = {'org': 'google', 'repos_url': ['google.com', 'holberton']}
        mock_json.return_value = value
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_pub:
            expected = ['google.com', 'holberton']
            mock_pub.return_value = expected
            new_org = GithubOrgClient('holberton')
            self.assertEqual(new_org.org(), value)
            self.assertEqual(new_org._public_repos_url, expected)
            mock_pub.assert_called_once()
            mock_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
