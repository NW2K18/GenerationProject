# Author: Nathan
# Unit tests for input_checker.py

import unittest
from unittest.mock import patch

import inputchecker


class TestInputChecker(unittest.TestCase):

    def test_check_index(self):
        self.assertTrue(inputchecker.check_index(10, '7'))
        self.assertTrue(inputchecker.check_index(10, '4'))
        self.assertTrue(inputchecker.check_index(10, '10'))

        self.assertFalse(inputchecker.check_index(10, '0'))
        self.assertFalse(inputchecker.check_index(10, 'Foobar'))

    @patch('builtins.input')
    def test_get_input_index(self, mock_input):
        mock_input.return_value = '0'

        self.assertEqual(mock_input(), '0')
        self.assertEqual(
            inputchecker.get_input_index('order', 'update', 10), None)
        mock_input.assert_called_with('Type the index of the \
order you wish to update: ')

        mock_input.return_value = '5'
        self.assertEqual(
            inputchecker.get_input_index('', '', 10), 4)

        mock_input.return_value = '5'
        self.assertEqual(
            inputchecker.get_input_index('', '', 10), 4)


if __name__ == '__main__':
    unittest.main()
