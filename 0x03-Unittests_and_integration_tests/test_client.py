#!/usr/bin/env python3
""" Testing client.py """
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
import client
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class MockResponse:
    """ A mock response object as a result for requests.get """

    def __init__(self, payload):
        self._payload = payload

    def json(self):
        """ returns the payload as a json """
        return self._payload


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_licence"}}, "my_licence", False),
    ])
    def test_has_license(self, test_repo, test_key, expected):
        """ Testing has_license method """
        self.assertEqual(
            GithubOrgClient.has_license(test_repo, test_key),
            expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration Testing for GithubOrgClient """

    @classmethod
    def setUpClass(cls):
        """ Setup testing mocks """
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [
            MockResponse(cls.org_payload),
            MockResponse(cls.repos_payload),
        ] * 2

    @classmethod
    def tearDownClass(cls):
        """ Stop testing mocks """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Testing public_repos method """
        obj = GithubOrgClient('a7a')
        repos = obj.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """ Testing public_repos_with_licence method """
        obj = GithubOrgClient('a7a')
        repos = obj.public_repos('apache-2.0')
        self.assertEqual(repos, self.apache2_repos)
