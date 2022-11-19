# Author: Nathan
# Unit tests for orderclass.py

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from ordermenu import Order_menu
from orderclass import Order
from productclass import Product
from courierclass import Courier


class TestOrderMenu(unittest.TestCase):

    @patch('ordermenu.Order_menu.load_orders')
    def setUp(
            self, mock_load: MagicMock):
        self.test_ordermenu = Order_menu()
        self.mock_load = mock_load
        self.test_ordermenu.orders.clear()
        self.test_ordermenu.orders.append(Order('Testname', 'Testtown',
                                          '0800001066'))
        self.test_ordermenu.orders[0].set_courier(11)
        self.test_ordermenu.orders[0].set_items('2,3')
        self.test_ordermenu.orders[0].set_order_status('3')
        self.test_ordermenu.orders.append(Order('Testname2', 'Testcity',
                                          '6601000080'))
        self.test_ordermenu.orders[1].set_courier(7)
        self.test_ordermenu.orders[1].set_items('5')
        self.test_ordermenu.orders[1].set_order_status('1')
        self.test_ordermenu.orders.append(Order('Testname3', 'Testcountry',
                                          '1066080000'))
        self.test_ordermenu.orders[2].set_courier(5)
        self.test_ordermenu.orders[2].set_items('4,5,8')
        self.test_ordermenu.orders[2].set_order_status('2')

        self.products = [
            Product('Test1', 0.75), Product('Test2', 1.00),
            Product('Test3', 1.50)]
        self.products[0].id = 3
        self.products[1].id = 5
        self.products[2].id = 8

        self.couriers = [
            Courier('TestA', '0800001066'), Courier('TestB', '6601000080'),
            Courier('TestC', '0080006610')]
        self.couriers[0].id = 5
        self.couriers[1].id = 7
        self.couriers[2].id = 11

        self.mock_productmenu = MagicMock()
        self.mock_couriermenu = MagicMock()
        self.mock_couriermenu.__str__ = 'CourierWoah'

    def test_setUp(
            self):
        self.mock_load.assert_called()

    @patch('ordermenu.sleep')
    @patch('builtins.print')
    def test_list_orders(
            self, mock_print: MagicMock, mock_sleep: MagicMock):
        list_length = self.test_ordermenu.list_orders(
            self.test_ordermenu.orders)

        self.assertEqual(list_length, 3)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(
            mock_print.mock_calls[0][1][0],
            'Order No.1 (0):'
            '\n\tCustomer name: Testname'
            '\n\tCustomer address: Testtown'
            '\n\tCustomer phone number: 0800001066'
            '\n\tCourier: 11 - COURIER HERE'
            '\n\tOrder status: Delivered'
            '\n\tItems: 2,3')
        self.assertEqual(
            mock_print.mock_calls[1][1][0],
            'Order No.2 (0):'
            '\n\tCustomer name: Testname2'
            '\n\tCustomer address: Testcity'
            '\n\tCustomer phone number: 6601000080'
            '\n\tCourier: 7 - COURIER HERE'
            '\n\tOrder status: Awaiting pickup'
            '\n\tItems: 5')
        self.assertEqual(
            mock_print.mock_calls[2][1][0],
            'Order No.3 (0):'
            '\n\tCustomer name: Testname3'
            '\n\tCustomer address: Testcountry'
            '\n\tCustomer phone number: 1066080000'
            '\n\tCourier: 5 - COURIER HERE'
            '\n\tOrder status: Out for delivery'
            '\n\tItems: 4,5,8')

    @patch('ordermenu.sleep')
    @patch('builtins.print')
    def test_list_sorted_orders(
            self, mock_print: MagicMock, mock_sleep: MagicMock):
        '''Test when option is courier.'''
        self.test_ordermenu.list_sorted_orders('courier')

        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(
            mock_print.mock_calls[0][1][0],
            'Order No.1 (0):'
            '\n\tCustomer name: Testname3'
            '\n\tCustomer address: Testcountry'
            '\n\tCustomer phone number: 1066080000'
            '\n\tCourier: 5 - COURIER HERE'
            '\n\tOrder status: Out for delivery'
            '\n\tItems: 4,5,8')
        self.assertEqual(
            mock_print.mock_calls[1][1][0],
            'Order No.2 (0):'
            '\n\tCustomer name: Testname2'
            '\n\tCustomer address: Testcity'
            '\n\tCustomer phone number: 6601000080'
            '\n\tCourier: 7 - COURIER HERE'
            '\n\tOrder status: Awaiting pickup'
            '\n\tItems: 5')
        self.assertEqual(
            mock_print.mock_calls[2][1][0],
            'Order No.3 (0):'
            '\n\tCustomer name: Testname'
            '\n\tCustomer address: Testtown'
            '\n\tCustomer phone number: 0800001066'
            '\n\tCourier: 11 - COURIER HERE'
            '\n\tOrder status: Delivered'
            '\n\tItems: 2,3')

    @patch('ordermenu.sleep')
    @patch('builtins.print')
    def test_list_sorted_orders2(
            self, mock_print: MagicMock, mock_sleep: MagicMock):
        '''Test when option is status.'''
        self.test_ordermenu.list_sorted_orders('status')

        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(
            mock_print.mock_calls[0][1][0],
            'Order No.1 (0):'
            '\n\tCustomer name: Testname2'
            '\n\tCustomer address: Testcity'
            '\n\tCustomer phone number: 6601000080'
            '\n\tCourier: 7 - COURIER HERE'
            '\n\tOrder status: Awaiting pickup'
            '\n\tItems: 5')
        self.assertEqual(
            mock_print.mock_calls[1][1][0],
            'Order No.2 (0):'
            '\n\tCustomer name: Testname3'
            '\n\tCustomer address: Testcountry'
            '\n\tCustomer phone number: 1066080000'
            '\n\tCourier: 5 - COURIER HERE'
            '\n\tOrder status: Out for delivery'
            '\n\tItems: 4,5,8')
        self.assertEqual(
            mock_print.mock_calls[2][1][0],
            'Order No.3 (0):'
            '\n\tCustomer name: Testname'
            '\n\tCustomer address: Testtown'
            '\n\tCustomer phone number: 0800001066'
            '\n\tCourier: 11 - COURIER HERE'
            '\n\tOrder status: Delivered'
            '\n\tItems: 2,3')

    @patch('ordermenu.sleep')
    @patch('builtins.print')
    def test_list_sorted_orders3(
            self, mock_print: MagicMock, mock_sleep: MagicMock):
        '''Test when option is invalid.'''
        try:
            self.test_ordermenu.list_sorted_orders('foobar')
            assert False
        except Exception:
            self.assertRaises(Exception)

    @patch('ordermenu.Order_menu.list_orders')
    @patch('ordermenu.sleep')
    @patch('builtins.print')
    def test_list_sorted_orders4(
            self, mock_print: MagicMock, mock_sleep: MagicMock,
            mock_list: MagicMock):
        '''Test to see if list_orders is called.'''
        self.test_ordermenu.list_sorted_orders('courier')
        mock_list.assert_called_once()

    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_create(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock):
        '''Test when all inputs are valid.'''
        mock_input.side_effect = ['Test4', 'Testplanet', '1122334455']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_create(
            self.mock_productmenu, self.mock_couriermenu)
        mock_get_courier.assert_called_once_with(self.mock_couriermenu)
        mock_get_items.assert_called_once_with(self.mock_productmenu)

        self.assertEqual(len(self.test_ordermenu.orders), 4)
        self.assertEqual(self.test_ordermenu.orders[3].id, 0)
        self.assertEqual(
            self.test_ordermenu.orders[3].customer_name, 'Test4')
        self.assertEqual(
            self.test_ordermenu.orders[3].customer_address, 'Testplanet')
        self.assertEqual(
            self.test_ordermenu.orders[3].customer_phone, '1122334455')
        self.assertEqual(self.test_ordermenu.orders[3].courier, 55)
        self.assertEqual(self.test_ordermenu.orders[3].status, 'Preparing')
        self.assertEqual(self.test_ordermenu.orders[3].items, '1,3,2')


if __name__ == '__main__':
    unittest.main()
