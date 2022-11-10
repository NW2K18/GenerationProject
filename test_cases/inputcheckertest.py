# Author: Nathan
# Unit tests for input_checker.py

import unittest
from unittest.mock import patch

import input_checker


def mock_input(input):
    return '0'


class TestInputChecker(unittest.TestCase):

    def test_check_index(self):
        self.assertTrue(input_checker.check_index(10, '7'))
        self.assertTrue(input_checker.check_index(10, '4'))
        self.assertTrue(input_checker.check_index(10, '10'))

        self.assertFalse(input_checker.check_index(10, '0'))
        self.assertFalse(input_checker.check_index(10, 'Foobar'))

    @patch('builtins.input')
    def test_get_input_index(self, mock_input):
        def foobarbranch():
            return 0
        self.assertEqual(input('input'), '0')
        self.assertEqual(
            input_checker.get_input_index('', '', 10), None)

        # mock_input.
        # self.assertEqual(
        #     input_checker.get_input_index('', '', 10), 4)



if __name__ == '__main__':
    unittest.main()
