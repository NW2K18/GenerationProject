# Author: Nathan
# Unit tests for main.py

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

import main


class TestMainMenu(unittest.TestCase):

    @patch('time.sleep')
    @patch('builtins.print')
    @patch('ordermenu.Order_menu')
    @patch('couriermenu.Courier_menu')
    @patch('productmenu.Product_menu')
    @patch('builtins.input')
    def test_main_option_exit(self, mock_input: MagicMock,
                              mock_product, mock_courier,
                              mock_order, mock_print: MagicMock, mock_sleep):
        mock_input.return_value = '0'
        testmenu = main.Menu()
        testmenu.main()
        mock_print.assert_called_with('Exitted!')

    @patch('time.sleep')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_product_menu_exit(self, mock_input: MagicMock,
                               mock_print: MagicMock, mock_sleep):
        mock_input.return_value = '0'
        testmenu = main.Menu()
        testmenu.view_products_menu()
        mock_print.assert_called_with('Exitting products menu...')
    
    @patch('time.sleep')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_courier_menu_exit(self, mock_input: MagicMock,
                               mock_print: MagicMock, mock_sleep):
        mock_input.return_value = '0'
        testmenu = main.Menu()
        testmenu.view_couriers_menu()
        mock_print.assert_called_with('Exitting couriers menu...')

    @patch('time.sleep')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_order_menu_exit(self, mock_input: MagicMock,
                             mock_print: MagicMock, mock_sleep):
        mock_input.return_value = '0'
        testmenu = main.Menu()
        testmenu.view_orders_menu()
        mock_print.assert_called_with('Exitting orders menu...')


if __name__ == '__main__':
    unittest.main()
