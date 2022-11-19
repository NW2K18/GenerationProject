"""Author: Nathan \n
Unit tests for input_checker.py
"""

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

import inputchecker
from productclass import Product
from courierclass import Courier


class TestInputChecker(unittest.TestCase):

    def setUp(self) -> None:
        self.couriers = [
            Courier('TestA', '0800001066'), Courier('TestB', '6601000080'),
            Courier('TestC', '0080006610')]
        self.couriers[0].id = 5
        self.couriers[1].id = 7
        self.couriers[2].id = 11

        self.products = [
            Product('Test1', 0.75), Product('Test2', 1.00),
            Product('Test3', 1.50)]
        self.products[0].id = 3
        self.products[1].id = 5
        self.products[2].id = 8

    def test_check_index(self):
        self.assertTrue(inputchecker.check_index(10, '1'))
        self.assertTrue(inputchecker.check_index(10, '4'))
        self.assertTrue(inputchecker.check_index(10, '10'))

        self.assertFalse(inputchecker.check_index(10, '0'))
        self.assertFalse(inputchecker.check_index(10, '15'))
        self.assertFalse(inputchecker.check_index(10, 'Foobar'))

    @patch('builtins.input')
    def test_get_input_index(self, mock_input: MagicMock):
        mock_input.return_value = '0'

        self.assertEqual(
            inputchecker.get_input_index('order', 'update', 10), None)
        mock_input.assert_called_with('Type the index of the \
order you wish to update: ')
        mock_input.assert_called_once()

        mock_input.return_value = '1'
        self.assertEqual(
            inputchecker.get_input_index('', '', 10), 0)

        mock_input.return_value = '5'
        self.assertEqual(
            inputchecker.get_input_index('', '', 10), 4)

        mock_input.return_value = '10'
        self.assertEqual(
            inputchecker.get_input_index('', '', 10), 9)

    def test_get_courier_id(
            self):
        '''With valid input.'''
        test_id = inputchecker.get_courier_id(self.couriers, '5')

        self.assertEqual(test_id, 5)

    def test_get_courier_id2(
            self):
        '''With invalid input.'''
        test_id = inputchecker.get_courier_id(self.couriers, '12')

        self.assertEqual(test_id, 0)

    def test_get_courier_id3(
            self):
        '''With invalid input.'''
        test_id = inputchecker.get_courier_id(self.couriers, 'foobar')

        self.assertEqual(test_id, 0)

    def test_get_item_id(
            self):
        '''With valid input.'''
        test_id = inputchecker.get_item_id(self.products, '8')

        self.assertEqual(test_id, '8')

    def test_get_item_id2(
            self):
        '''With invalid input.'''
        test_id = inputchecker.get_item_id(self.products, '12')

        self.assertEqual(test_id, None)

    def test_get_item_id3(
            self):
        '''With invalid input.'''
        test_id = inputchecker.get_item_id(self.products, 'foobar')

        self.assertEqual(test_id, None)


if __name__ == '__main__':
    unittest.main()
