#!/usr/bin/env python3
"""Module to test the client.py file functions"""


from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest import TestCase, mock
from mock import patch


class TestGithubOrgClient(TestCase):
    """Test for GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json",
           mock.MagicMock(return_value={'key': 'value'}))
    def test_org(self, org_name):
        "test org method"
        cli = GithubOrgClient(org_name)
        self.assertEqual(cli.org, {'key': 'value'})

    def test_public_repos_url(self):
        """Test public_repos_url method"""
        with mock.patch("client.get_json",
                   new_callable=mock.PropertyMock,
                   return_value={"repos_url": "url"}):
            cli = GithubOrgClient("google")
            self.assertEqual(cli._public_repos_url, "url")

    @patch('client.get_json')
    def test_public_repos(self, mocker):
        """test public repos methods"""
        mocker.return_value = [{'org': 'tesla'}]
        test = GithubOrgClient('tesls')
        with mock.patch('client.GithubOrgClient._public_repos_url',
                   new_callable=mock.PropertyMock) as mock:
            mock.return_value = 'tesla'
            self.assertEqual(test.public_repos(), ['tesla'])
            mock.assert_called_once()
            mocker.assert_called_once()
