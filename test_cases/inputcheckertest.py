"""Author: Nathan \n
Unit tests for input_checker.py
"""

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

import inputchecker
from productclass import Product
from courierclass import Courier
from orderclass import Order


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

        self.orders = [
            Order('TestX', 'Testtown', '0900001077'),
            Order('TestY', 'Testcountry', '0900001078'),
            Order('TestZ', 'Testcity', '0900001079')]
        self.orders[0].id = 50
        self.orders[1].id = 100
        self.orders[2].id = 150

    def test_check_index(self):
        self.assertTrue(inputchecker.check_index(10, '1'))
        self.assertTrue(inputchecker.check_index(10, '4'))
        self.assertTrue(inputchecker.check_index(10, '10'))

        self.assertFalse(inputchecker.check_index(10, '0'))
        self.assertFalse(inputchecker.check_index(10, '15'))
        self.assertFalse(inputchecker.check_index(10, 'Foobar'))

    @patch('builtins.input')
    def test_get_input_index(
            self, mock_input: MagicMock):
        '''Test with input 0.'''
        mock_input.return_value = '0'
        mock_list = MagicMock()

        self.assertEqual(
            inputchecker.get_input_index(
                'product', 'update', mock_list), None)
        mock_input.assert_called_once_with(
            'Type the ID of the '
            'product you wish to update(0 to exit): ')

    @patch('inputchecker.get_product_index')
    @patch('builtins.input')
    def test_get_input_index2(
            self, mock_input: MagicMock, mock_check: MagicMock):
        '''Test with update product.'''
        mock_input.return_value = '7'
        mock_list = MagicMock()
        mock_check.return_value = 5

        self.assertEqual(
            inputchecker.get_input_index(
                'product', 'update', mock_list), 5)
        mock_check.assert_called_once_with(mock_list, '7')
        mock_input.assert_called_once_with(
            'Type the ID of the '
            'product you wish to update(0 to exit): ')

    @patch('inputchecker.get_product_index')
    @patch('builtins.input')
    def test_get_input_index3(
            self, mock_input: MagicMock, mock_check: MagicMock):
        '''Test with remove product.'''
        mock_input.return_value = '9'
        mock_list = MagicMock()
        mock_check.return_value = 7

        self.assertEqual(
            inputchecker.get_input_index(
                'product', 'remove', mock_list), 7)
        mock_check.assert_called_once_with(mock_list, '9')
        mock_input.assert_called_once_with(
            'Type the ID of the '
            'product you wish to remove(0 to exit): ')

    @patch('inputchecker.get_courier_index')
    @patch('builtins.input')
    def test_get_input_index4(
            self, mock_input: MagicMock, mock_check: MagicMock):
        '''Test with update courier.'''
        mock_input.return_value = '87'
        mock_list = MagicMock()
        mock_check.return_value = 65

        self.assertEqual(
            inputchecker.get_input_index(
                'courier', 'update', mock_list), 65)
        mock_check.assert_called_once_with(mock_list, '87')
        mock_input.assert_called_once_with(
            'Type the ID of the '
            'courier you wish to update(0 to exit): ')

    @patch('inputchecker.get_courier_index')
    @patch('builtins.input')
    def test_get_input_index5(
            self, mock_input: MagicMock, mock_check: MagicMock):
        '''Test with remove courier.'''
        mock_input.return_value = '87'
        mock_list = MagicMock()
        mock_check.return_value = 65

        self.assertEqual(
            inputchecker.get_input_index(
                'courier', 'remove', mock_list), 65)
        mock_check.assert_called_once_with(mock_list, '87')
        mock_input.assert_called_once_with(
            'Type the ID of the '
            'courier you wish to remove(0 to exit): ')

    @patch('inputchecker.get_order_index')
    @patch('builtins.input')
    def test_get_input_index6(
            self, mock_input: MagicMock, mock_check: MagicMock):
        '''Test with update order'''
        mock_input.return_value = '87'
        mock_list = MagicMock()
        mock_check.return_value = 65

        self.assertEqual(
            inputchecker.get_input_index(
                'order', 'update', mock_list), 65)
        mock_check.assert_called_once_with(mock_list, '87')
        mock_input.assert_called_once_with(
            'Type the ID of the '
            'order you wish to update(0 to exit): ')

    @patch('inputchecker.get_order_index')
    @patch('builtins.input')
    def test_get_input_index7(
            self, mock_input: MagicMock, mock_check: MagicMock):
        '''Test with remove order'''
        mock_input.return_value = '87'
        mock_list = MagicMock()
        mock_check.return_value = 65

        self.assertEqual(
            inputchecker.get_input_index(
                'order', 'remove', mock_list), 65)
        mock_check.assert_called_once_with(mock_list, '87')
        mock_input.assert_called_once_with(
            'Type the ID of the '
            'order you wish to remove(0 to exit): ')

    @patch('builtins.input')
    def test_get_input_index8(
            self, mock_input: MagicMock):
        '''Test with invalid option'''
        mock_input.return_value = '87'
        mock_list = MagicMock()

        with self.assertRaises(Exception):
            inputchecker.get_input_index(
                'foobar', 'update', mock_list)

    def test_sanitise_input(self):
        # Normal input.
        result = inputchecker.sanitise_input('Test45 Name')
        self.assertEqual(result, 'Test45 Name')

        # Empty input.
        result = inputchecker.sanitise_input('')
        self.assertEqual(result, '')

        # Input with special characters
        result = inputchecker.sanitise_input('Test/Name.Admin < Something')
        self.assertEqual(result, 'Test/Name.Admin &lt; Something')

    def test_validate_phone(
            self):
        result = inputchecker.validate_phone('1122334455')
        self.assertEqual(result, '1122334455')

        result = inputchecker.validate_phone('11223344556')
        self.assertEqual(result, '11223344556')

        result = inputchecker.validate_phone('112233445')
        self.assertEqual(result, '')

        result = inputchecker.validate_phone('1122334455test')
        self.assertEqual(result, '')

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

    def test_get_item_quantity(
            self):
        items = '2, 2, 2, 3, 3, 5'
        result = inputchecker.get_item_quantity(items)

        self.assertEqual(
            result, {'2': 3, '3': 2, '5': 1})

    def test_get_product_index(
            self):
        self.assertEqual(
            inputchecker.get_product_index(self.products, '8'), 2)
        self.assertEqual(
            inputchecker.get_product_index(self.products, '9'), None)

    def test_get_courier_index(
            self):
        self.assertEqual(
            inputchecker.get_courier_index(self.couriers, '7'), 1)
        self.assertEqual(
            inputchecker.get_courier_index(self.couriers, '8'), None)

    def test_get_order_index(
            self):
        self.assertEqual(
            inputchecker.get_order_index(self.orders, '50'), 0)
        self.assertEqual(
            inputchecker.get_order_index(self.orders, '55'), None)


if __name__ == '__main__':
    unittest.main()
