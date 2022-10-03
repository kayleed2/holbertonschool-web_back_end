#!/usr/bin/env python3
"""Module to test the utils.py file functions"""
import unittest
from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test for access nested map function"""
    @parameterized.expand([
       ({"a": 1}, ("a",), 1),
       ({"a": {"b": 2}}, ("a",), {"b": 2}),
       ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expect):
        """Test the access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expect)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expect):
        """Test accesss nested map exception"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class to implement test get JSON"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Test the get_json function"""
        with mock.patch("requests.get") as get:
            get.return_value.json.return_value = payload
            self.assertEqual(get_json(url), payload)


class TestMemoize(TestCase):
    """Test memoize"""

    def test_memoize(self):
        """Test asserting memoize sets attribute"""
        class TestClass:
            """The test class for memoize module"""
            def a_method(self):
                """Test the a_method function"""
                return 42

            @memoize
            def a_property(self):
                """test a_property function"""
                return self.a_method()
