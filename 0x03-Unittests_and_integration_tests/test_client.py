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

    @patch('client.get_json')  # patching request.get will do same thing
    def test_public_repos(self, mock_get_json):
        """unit-test for GithubOrgClient.public_repos."""
        mock_payload = [{'name': 'google'}]
        mock_get_json.return_value = mock_payload
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_pub:
            expected_pub_rep_url = 'http://spacedigit.tech'
            mock_pub.return_value = expected_pub_rep_url
            new_org = GithubOrgClient('holberton')
            self.assertEqual(new_org.public_repos(), ['google'])

            mock_pub.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),

    ])
    def test_has_license(self, nested_map, path, expected):
        """Unit-test for GithubOrgClient.has_license."""
        self.assertEqual(
            GithubOrgClient.has_license(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
