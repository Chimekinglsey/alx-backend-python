#!/usr/bin/env python3
"""This module contains unittests for clients.py
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch, PropertyMock

from requests import HTTPError
from client import GithubOrgClient
from typing import Dict
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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
    @patch.object(GithubOrgClient, 'has_license')
    def test_has_license(self, repo: Dict[str, Dict], license_key: str,
                         expected_result: bool, mock_has_lincense) -> None:
        """Unit-test for GithubOrgClient.has_license."""
        mock_has_lincense.return_value = expected_result
        org = GithubOrgClient('holberton')
        result = org.has_license(repo, license_key)
        self.assertEqual(expected_result, result)


@parameterized_class(
    ('payload', 'value'),
    [
        ('org_payload', org_payload),
        ('repos_payload', repos_payload),
        ('expected_repos', expected_repos),
        ('apache2_repos', apache2_repos),
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration Testing"""
    @classmethod
    def setUpClass(cls) -> None:
        """Initiates before class execution"""
        cls.expected_payloads = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def fetch_payload(url):
            """Retrieves payload if exists in the expected_payloads dict"""
            if url in cls.expected_payloads:
                return Mock(spec=['json'], json=Mock(
                    return_value=cls.expected_payloads[url]))
            raise HTTPError

        cls.get_mock = patch('requests.get')
        cls.get_patcher = cls.get_mock.start()
        cls.get_patcher.return_value.json.side_effect = fetch_payload
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """cleans up setup class attributes"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
