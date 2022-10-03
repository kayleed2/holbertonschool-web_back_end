#!/usr/bin/env python3
"""Module to test the client.py file functions"""


from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """Test for GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json",
           mock.MagicMock(return_value={'key': 'value'}))
    def test_org(self, org_name):
        "test the org method"
        cli = GithubOrgClient(org_name)
        self.assertEqual(cli.org, {'key': 'value'})

    def test_public_repos_url(self):
        """Test public_repos_url method"""
        with patch("client.get_json",
                   new_callable=mock.PropertyMock,
                   return_value={"repos_url": "url"}):
            cli = GithubOrgClient("google")
            self.assertEqual(cli._public_repos_url, "url")

    @patch('client.get_json')
    def test_public_repos(self, mocker):
        """test public repos methods"""
        mocker.return_value = [{'org': 'tesla'}]
        test = GithubOrgClient('tesla')
        with mock.patch('client.GithubOrgClient._public_repos_url',
                        new_callable=mock.PropertyMock) as mock:
            mock.return_value = 'tesla'
            self.assertEqual(test.public_repos(), ['tesla'])
            mock.assert_called_once()
            mocker.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test for the has_license method"""
        cli = GithubOrgClient('org_name')
        self.assertEqual(cli.has_license(repo, license_key), expected)

@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Create the TestIntegrationGithubOrgClient class and
    implement the setUpClass and tearDownClass"""

    @classmethod
    def setUpClass(cls):
        """Set up class for tests"""
        from urllib.error import HTTPError
        cls.get_patcher = patch("requests.get", side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """Teardown for tests"""
        cls.get_patcher.stop()
