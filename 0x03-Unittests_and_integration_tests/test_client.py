#!/usr/bin/env python3
""" Testing client.py """
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient class """

    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, test_org, mock):
        """ Testing org property """
        assert client.get_json is mock
        obj = GithubOrgClient(test_org)
        obj.org
        mock.assert_called_once_with(
                f'https://api.github.com/orgs/{test_org}')

    def test_public_repos_url(self):
        """ Testing _public_repos_url property  """
        PAYLOAD = 'a7a'
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock) as mock:
            mock.return_value = {
                "repos_url": PAYLOAD,
            }
            obj = GithubOrgClient('another a7a')
            self.assertEqual(obj._public_repos_url, PAYLOAD)

    @patch('client.get_json', return_value=[
        {'name': 'a7a1'},
        {'name': 'a7a2'},
    ])
    def test_public_repos(self, json_mock):
        """ Testing public_repos method """
        assert client.get_json is json_mock

        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as public_mock:

            public_mock.return_value = 'a7a'

            obj = GithubOrgClient('a7a')
            results = obj.public_repos()
            self.assertEqual(results, ['a7a1', 'a7a2'])

            json_mock.assert_called_once()
            public_mock.assert_called_once()