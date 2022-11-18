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
    @patch('database.Database')
    def setUp(
            self, mock_database: MagicMock, mock_load_database: MagicMock):
        self.testmenu = Product_menu()
        self.testdatabase = mock_database
        self.testload_on_startup = mock_load_database
        self.testmenu.products.clear()
        self.testmenu.products = [
            Product('Test1', 0.75), Product('Test2', 1.00),
            Product('Test3', 1.50)]

    def test_setUp(
            self):
        self.testload_on_startup.assert_called()

    @patch('main.sleep')
    @patch('builtins.print')
    def test_list_products(
            self, mock_print: MagicMock, mock_sleep: MagicMock):
        list_length = self.testmenu.list_products()

        self.assertEqual(list_length, 3)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(
            mock_print.mock_calls[0][1][0],
            'Product No.1 (0):'
            '\n\tProduct name: Test1'
            '\n\tProduct price: £0.75')
        self.assertEqual(
            mock_print.mock_calls[1][1][0],
            'Product No.2 (0):'
            '\n\tProduct name: Test2'
            '\n\tProduct price: £1.00')
        self.assertEqual(
            mock_print.mock_calls[2][1][0],
            'Product No.3 (0):'
            '\n\tProduct name: Test3'
            '\n\tProduct price: £1.50')
        pass

    def test_load_products_csv(
            self):
        pass

    def test_save_products_csv(
            self):
        pass

    def test_load_products_database(
            self):
        pass

    def test_save_products_database(
            self):
        pass

    def test_set_product_create(
            self):
        pass

    def test_set_product_update(
            self):
        pass

    def test_set_product_remove(
            self):
        pass


if __name__ == '__main__':
    unittest.main()
