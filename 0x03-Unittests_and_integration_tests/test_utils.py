#!/usr/bin/env python3
""" Unit testing for utils """

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
import requests
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Testing access_nested_map function """

    @parameterized.expand([
        ({"a": 1}, ("a", ), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Testing the function access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a", ), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested, path, key):
        """ Testing exceptions for access_nested_map function """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested, path)
        self.assertEqual((key, ), err.exception.args)


class TestGetJson(unittest.TestCase):
    """ Testing get_json function """

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json function for results """

        class MockObj:
            """ Mock Object For Testing """

            def __init__(self, payload):
                self.__payload = payload

            def json(self):
                """ return mock json payload """
                return self.__payload

        requests.get = Mock(return_value=MockObj(test_payload))
        value = get_json(test_url)
        self.assertEqual(value, test_payload)


class TestMemoize(unittest.TestCase):
    """ Testing memoized decorator """

    def test_memoize(self):
        """ Test the decorator """

        class TestClass:
            """ Testing class """

            def a_method(self):
                """ testing method """
                return 42

            @memoize
            def a_property(self):
                """ testing property """
                return self.a_method()


        obj = TestClass()
        self.assertEqual(obj.a_property, 42)
        self.assertEqual(obj.a_property, 42)

        obj = TestClass()
        with patch.object(obj, 'a_method') as mock:
            obj.a_property
            obj.a_property
            mock.assert_called_once()
