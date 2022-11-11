# Author: Nathan
# Unit tests for main.py

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

import main


class TestMainMenu(unittest.TestCase):

    @patch('ordermenu.Order_menu')
    @patch('couriermenu.Courier_menu')
    @patch('productmenu.Product_menu')
    def setUp(self, mock_product: MagicMock, mock_courier: MagicMock,
              mock_order: MagicMock):
        self.testmenu = main.Menu()
        self.mock_product = mock_product
        self.mock_product.reset_mock()
        self.mock_courier = mock_courier
        self.mock_courier.reset_mock()
        self.mock_order = mock_order
        self.mock_order.reset_mock()


    @patch('main.sleep')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_main_option_exit(self, mock_input: MagicMock,
                              mock_print: MagicMock,
                              mock_sleep: MagicMock):
        mock_input.return_value = '0'
        self.testmenu.main()
        mock_print.assert_called_with('Exitted!')
        self.assertEqual(mock_print.call_count, 3)
        mock_sleep.assert_not_called()

    @patch('main.sleep')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_product_menu_exit(self, mock_input: MagicMock,
                               mock_print: MagicMock, mock_sleep: MagicMock):
        mock_input.return_value = '0'
        self.testmenu.view_products_menu()
        mock_print.assert_called_with('Exitting products menu...')
        self.assertEqual(mock_print.call_count, 2)
        mock_sleep.assert_called_once()

    @patch('main.sleep')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_product_menu_create(self, mock_input: MagicMock,
                                 mock_print: MagicMock, mock_sleep: MagicMock,
                                 ):
        mock_input.side_effect = ['1', '0']
        self.testmenu.view_products_menu()
        mock_print.assert_called_with('Exitting products menu...')
        self.assertEqual(self.mock_product.mock_calls[0][0],
                         '().set_product_create')

    @patch('main.sleep')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_courier_menu_exit(self, mock_input: MagicMock,
                               mock_print: MagicMock, mock_sleep: MagicMock):
        mock_input.return_value = '0'
        self.testmenu.view_couriers_menu()
        mock_print.assert_called_with('Exitting couriers menu...')
        self.assertEqual(mock_print.call_count, 2)
        mock_sleep.assert_called_once()

    @patch('main.sleep')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_order_menu_exit(self, mock_input: MagicMock,
                             mock_print: MagicMock, mock_sleep: MagicMock):
        mock_input.return_value = '0'
        self.testmenu.view_orders_menu()
        mock_print.assert_called_with('Exitting orders menu...')
        self.assertEqual(mock_print.call_count, 2)
        mock_sleep.assert_called_once()


if __name__ == '__main__':
    unittest.main()
