"""Author: Nathan \n
Unit tests for productmenu.py
"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from productmenu import Product_menu
from productclass import Product


class TestProductMenu(unittest.TestCase):

    @patch('productmenu.Product_menu.load_products_database')
    @patch('productmenu.Database')
    def setUp(
            self, mock_database: MagicMock, mock_database_load: MagicMock):
        self.testmenu = Product_menu()
        self.mock_database = mock_database
        mock_database.reset_mock()
        self.mock_database_load = mock_database_load
        self.testmenu.products.clear()
        self.testmenu.products = [
            Product('Test1', 0.75), Product('Test2', 1.00),
            Product('Test3', 1.50)]

    def test_setUp(
            self):
        self.mock_database_load.assert_called()

    @patch('productmenu.sleep')
    @patch('builtins.print')
    def test_list_products(
            self, mock_print: MagicMock, mock_sleep: MagicMock):
        list_length = self.testmenu.list_products()

        self.assertEqual(list_length, 3)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(
            mock_print.mock_calls[0][1][0],
            'Product No.0:'
            '\n\tProduct name: Test1'
            '\n\tProduct price: £0.75')
        self.assertEqual(
            mock_print.mock_calls[1][1][0],
            'Product No.0:'
            '\n\tProduct name: Test2'
            '\n\tProduct price: £1.00')
        self.assertEqual(
            mock_print.mock_calls[2][1][0],
            'Product No.0:'
            '\n\tProduct name: Test3'
            '\n\tProduct price: £1.50')

    def test_load_products_database(
            self):
        self.mock_database.return_value.load_products.return_value = [
            {'id': 4, 'name': 'dTest', 'price': 1.45},
            {'id': 27, 'name': 'dTest2', 'price': 1.85}]

        self.testmenu.load_products_database()
        self.assertEqual(self.testmenu.products[0].id, 4)
        self.assertEqual(self.testmenu.products[0].name, 'dTest')
        self.assertEqual(self.testmenu.products[0].price, 1.45)
        self.assertEqual(self.testmenu.products[1].id, 27)
        self.assertEqual(self.testmenu.products[1].name, 'dTest2')
        self.assertEqual(self.testmenu.products[1].price, 1.85)

    def test_save_products_database(
            self):
        self.testmenu.save_products_database()
        self.assertEqual(
            self.mock_database.mock_calls[0][0], '().save_products')
        self.assertEqual(
            self.mock_database.mock_calls[0][1][0], self.testmenu.products)

    @patch('productmenu.datalogger')
    @patch('builtins.input')
    def test_set_product_create(
            self, mock_input: MagicMock, mock_logger: MagicMock):
        mock_input.side_effect = ['Test4', '50.50']
        self.mock_database.return_value.insert_product.return_value = 50

        self.testmenu.set_product_create()
        self.assertEqual(self.testmenu.products[3].id, 50)
        self.assertEqual(self.testmenu.products[3].name, 'Test4')
        self.assertEqual(self.testmenu.products[3].price, 50.50)
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_create')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Product: Test4',))

    @patch('productmenu.datalogger')
    @patch('builtins.input')
    def test_set_product_update1(
            self, mock_input: MagicMock, mock_logger: MagicMock):
        '''Test with all inputs full.'''
        mock_input.side_effect = ['Test4', '50.50']

        self.testmenu.set_product_update(1)
        self.assertEqual(self.testmenu.products[1].name, 'Test4')
        self.assertEqual(self.testmenu.products[1].price, 50.50)
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Product: Test4',))

    @patch('productmenu.datalogger')
    @patch('builtins.input')
    def test_set_product_update2(
            self, mock_input: MagicMock, mock_logger: MagicMock):
        '''Test with name blank.'''
        mock_input.side_effect = ['', '51.60']
        self.testmenu.set_product_update(1)
        self.assertEqual(self.testmenu.products[1].name, 'Test2')
        self.assertEqual(self.testmenu.products[1].price, 51.60)
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Product: Test2',))

    @patch('productmenu.datalogger')
    @patch('builtins.input')
    def test_set_product_update3(
            self, mock_input: MagicMock, mock_logger: MagicMock):
        '''Test with price blank.'''
        mock_input.side_effect = ['Test5', '']
        self.testmenu.set_product_update(1)
        self.assertEqual(self.testmenu.products[1].name, 'Test5')
        self.assertEqual(self.testmenu.products[1].price, 1.00)
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Product: Test5',))

    @patch('productmenu.datalogger')
    @patch('builtins.input')
    def test_set_product_update4(
            self, mock_input: MagicMock, mock_logger: MagicMock):
        '''Test with all inputs blank.'''
        mock_input.side_effect = ['', '']
        self.testmenu.set_product_update(1)
        self.assertEqual(self.testmenu.products[1].name, 'Test2')
        self.assertEqual(self.testmenu.products[1].price, 1.00)
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Product: Test2',))

    @patch('productmenu.datalogger')
    @patch('builtins.input')
    def test_set_product_update5(
            self, mock_input: MagicMock, mock_logger: MagicMock):
        '''Test with invalid price entered.'''
        mock_input.side_effect = ['Test5', 'Test6']
        self.testmenu.set_product_update(1)
        self.assertRaises(ValueError)
        self.assertEqual(self.testmenu.products[1].name, 'Test5')
        self.assertEqual(self.testmenu.products[1].price, 1.00)
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Product: Test5',))

    @patch('productmenu.datalogger')
    def test_set_product_remove(
            self, mock_logger: MagicMock):
        removed_product = self.testmenu.products[1]

        result = self.testmenu.set_product_remove(1)
        self.assertEqual(
            self.mock_database.mock_calls[0][0], '().remove_product')
        self.assertEqual(
            self.mock_database.mock_calls[0].args, (removed_product,))
        self.assertEqual(len(self.testmenu.products), 2)
        self.assertEqual(result, 'Test2')
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_remove')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Product: Test2',))


if __name__ == '__main__':
    unittest.main()
