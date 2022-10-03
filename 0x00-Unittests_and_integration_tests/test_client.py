#!/usr/bin/env python3
"""Module to test the client.py file functions"""


from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest import TestCase, mock


class TestGithubOrgClient(TestCase):
    """Test for GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @mock.patch("client.get_json",
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
