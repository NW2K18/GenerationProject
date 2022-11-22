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

    @patch('ordermenu.Database')
    @patch('ordermenu.Order_menu.load_orders_database')
    def setUp(
            self, mock_load: MagicMock, mock_database: MagicMock):
        self.test_ordermenu = Order_menu()
        self.mock_database = mock_database
        self.mock_load = mock_load
        self.test_ordermenu.orders.clear()
        self.test_ordermenu.orders.append(Order('Testname', 'Testtown',
                                          '0800001066'))
        self.test_ordermenu.orders[0].id = 6
        self.test_ordermenu.orders[0].set_courier(11)
        self.test_ordermenu.orders[0].set_items('2,3')
        self.test_ordermenu.orders[0].set_order_status('4')
        self.test_ordermenu.orders.append(Order('Testname2', 'Testcity',
                                          '6601000080'))
        self.test_ordermenu.orders[1].id = 13
        self.test_ordermenu.orders[1].set_courier(7)
        self.test_ordermenu.orders[1].set_items('5')
        self.test_ordermenu.orders[1].set_order_status('2')
        self.test_ordermenu.orders.append(Order('Testname3', 'Testcountry',
                                          '1066080000'))
        self.test_ordermenu.orders[2].id = 21
        self.test_ordermenu.orders[2].set_courier(5)
        self.test_ordermenu.orders[2].set_items('4,5,8')
        self.test_ordermenu.orders[2].set_order_status('3')

        self.mock_productmenu = MagicMock()
        self.mock_couriermenu = MagicMock()

        self.couriers = [
            Courier('TestA', '0800001066'), Courier('TestB', '6601000080'),
            Courier('TestC', '0080006610')]

        self.products = [
            Product('Test1', 0.75), Product('Test2', 1.00),
            Product('Test3', 1.50), Product('Test4', 2.50),
            Product('Test5', 3.50), Product('Test6', 5.00)]

    def test_setUp(
            self):
        self.mock_load.assert_called()

    @patch('inputchecker.get_product_index')
    @patch('inputchecker.get_courier_index')
    @patch('ordermenu.sleep')
    @patch('builtins.print')
    def test_list_orders(
            self, mock_print: MagicMock, mock_sleep: MagicMock,
            mock_ccheck: MagicMock, mock_pcheck: MagicMock):
        mock_ccheck.side_effect = [2, 1, 0]
        mock_pcheck.side_effect = [0, 1, 3, 2, 4, 5]

        list_length = self.test_ordermenu.list_orders(
            self.test_ordermenu.orders, self.products,
            self.couriers)

        self.assertEqual(list_length, 3)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(
            mock_print.mock_calls[0][1][0],
            'Order No.6:'
            '\n\tCustomer name: Testname'
            '\n\tCustomer address: Testtown'
            '\n\tCustomer phone number: 0800001066'
            '\n\tCourier: 11 - TestC'
            '\n\tOrder status: Delivered'
            '\n\tItems:'
            '\n\t\tTest1 - £0.75'
            '\n\t\tTest2 - £1.00')
        self.assertEqual(
            mock_print.mock_calls[1][1][0],
            'Order No.13:'
            '\n\tCustomer name: Testname2'
            '\n\tCustomer address: Testcity'
            '\n\tCustomer phone number: 6601000080'
            '\n\tCourier: 7 - TestB'
            '\n\tOrder status: Awaiting pickup'
            '\n\tItems:'
            '\n\t\tTest4 - £2.50')
        self.assertEqual(
            mock_print.mock_calls[2][1][0],
            'Order No.21:'
            '\n\tCustomer name: Testname3'
            '\n\tCustomer address: Testcountry'
            '\n\tCustomer phone number: 1066080000'
            '\n\tCourier: 5 - TestA'
            '\n\tOrder status: Out for delivery'
            '\n\tItems:'
            '\n\t\tTest3 - £1.50'
            '\n\t\tTest5 - £3.50'
            '\n\t\tTest6 - £5.00')

    @patch('ordermenu.Order_menu.list_orders')
    @patch('ordermenu.sleep')
    @patch('builtins.print')
    def test_list_sorted_orders(
            self, mock_print: MagicMock, mock_sleep: MagicMock,
            mock_list: MagicMock):
        '''Test when option is courier.'''
        self.test_ordermenu.list_sorted_orders(
            'courier', MagicMock, MagicMock)
        sorted_list = mock_list.mock_calls[0].args[0]

        self.assertEqual(sorted_list[0], self.test_ordermenu.orders[2])
        self.assertEqual(sorted_list[1], self.test_ordermenu.orders[1])
        self.assertEqual(sorted_list[2], self.test_ordermenu.orders[0])

    @patch('ordermenu.Order_menu.list_orders')
    @patch('ordermenu.sleep')
    @patch('builtins.print')
    def test_list_sorted_orders2(
            self, mock_print: MagicMock, mock_sleep: MagicMock,
            mock_list: MagicMock):
        '''Test when option is status.'''
        self.test_ordermenu.list_sorted_orders(
            'status', MagicMock, MagicMock)
        sorted_list = mock_list.mock_calls[0].args[0]

        self.assertEqual(sorted_list[0], self.test_ordermenu.orders[1])
        self.assertEqual(sorted_list[1], self.test_ordermenu.orders[2])
        self.assertEqual(sorted_list[2], self.test_ordermenu.orders[0])

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
        self.test_ordermenu.list_sorted_orders(
            'courier', MagicMock, MagicMock)
        mock_list.assert_called_once()

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_create1(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when all inputs are valid.'''
        mock_input.side_effect = ['Test4', 'Testplanet', '1122334455']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'
        self.mock_database.return_value.insert_order.return_value = 0

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
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_create')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Test4\'s order',))

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_create2(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when name is blank'''
        mock_input.side_effect = ['', 'Testplanet', '1122334455']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_create(
            self.mock_productmenu, self.mock_couriermenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_create3(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when address is blank'''
        mock_input.side_effect = ['Test4', '', '1122334455']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_create(
            self.mock_productmenu, self.mock_couriermenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_create4(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when phone is blank'''
        mock_input.side_effect = ['Test4', 'Testplanet', '']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_create(
            self.mock_productmenu, self.mock_couriermenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_create5(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when courier id is blank'''
        mock_input.side_effect = ['Test4', 'Testplanet', '1122334455']
        mock_get_courier.return_value = 0
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_create(
            self.mock_productmenu, self.mock_couriermenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_create6(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when item IDs are blank'''
        mock_input.side_effect = ['Test4', 'Testplanet', '1122334455']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = ''

        self.test_ordermenu.set_order_create(
            self.mock_productmenu, self.mock_couriermenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_create7(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when phone is invalid'''
        mock_input.side_effect = ['Test4', 'Testplanet', 'foobar']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_create(
            self.mock_productmenu, self.mock_couriermenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)

    @patch('inputchecker.get_courier_id')
    @patch('builtins.input')
    def test_set_order_get_courier(
            self, mock_input: MagicMock, mock_checker: MagicMock):
        mock_input.side_effect = ['5']
        mock_checker.return_value = 5

        test_return = self.test_ordermenu.set_order_get_courier(
            self.mock_couriermenu)

        self.mock_couriermenu.list_couriers.assert_called_once()
        mock_checker.assert_called_once_with(
            self.mock_couriermenu.couriers, '5')
        self.assertEqual(test_return, 5)

    @patch('inputchecker.get_item_id')
    @patch('builtins.input')
    def test_set_order_get_items(
            self, mock_input: MagicMock, mock_checker: MagicMock):
        '''Test when looped 3 times.'''
        mock_input.side_effect = ['5', '8', '21', '']
        mock_checker.side_effect = ['5', '8', '21']

        test_return = self.test_ordermenu.set_order_get_items(
            self.mock_productmenu)

        self.assertEqual(
            self.mock_productmenu.list_products.call_count, 4)
        self.assertEqual(mock_checker.call_count, 3)
        self.assertEqual(
            mock_checker.mock_calls[0].args, (
                self.mock_productmenu.products, '5'))
        self.assertEqual(
            mock_checker.mock_calls[1].args, (
                self.mock_productmenu.products, '8'))
        self.assertEqual(
            mock_checker.mock_calls[2].args, (
                self.mock_productmenu.products, '21'))
        self.assertEqual(test_return, '5, 8, 21')

    @patch('inputchecker.get_item_id')
    @patch('builtins.input')
    def test_set_order_get_items2(
            self, mock_input: MagicMock, mock_checker: MagicMock):
        '''Test when looped once'''
        mock_input.side_effect = ['5', '']
        mock_checker.side_effect = ['5']

        test_return = self.test_ordermenu.set_order_get_items(
            self.mock_productmenu)

        self.assertEqual(
            self.mock_productmenu.list_products.call_count, 2)
        self.assertEqual(mock_checker.call_count, 1)
        self.assertEqual(
            mock_checker.mock_calls[0].args, (
                self.mock_productmenu.products, '5'))
        self.assertEqual(test_return, '5')

    @patch('inputchecker.get_item_id')
    @patch('builtins.input')
    def test_set_order_get_items3(
            self, mock_input: MagicMock, mock_checker: MagicMock):
        '''Test when looped zero times.'''
        mock_input.side_effect = ['']

        test_return = self.test_ordermenu.set_order_get_items(
            self.mock_productmenu)

        self.assertEqual(
            self.mock_productmenu.list_products.call_count, 1)
        self.assertEqual(mock_checker.call_count, 0)
        self.assertEqual(test_return, '')

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_update1(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when all inputs are valid.'''
        mock_input.side_effect = ['Test4', 'Testplanet', '1122334455']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_update(
            1, self.mock_productmenu, self.mock_couriermenu)
        mock_get_courier.assert_called_once_with(self.mock_couriermenu)
        mock_get_items.assert_called_once_with(self.mock_productmenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_name, 'Test4')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_address, 'Testplanet')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_phone, '1122334455')
        self.assertEqual(self.test_ordermenu.orders[1].courier, 55)
        self.assertEqual(self.test_ordermenu.orders[1].items, '1,3,2')
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Test4\'s order',))

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_update2(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when name is blank'''
        mock_input.side_effect = ['', 'Testplanet', '1122334455']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_update(
            1, self.mock_productmenu, self.mock_couriermenu)
        mock_get_courier.assert_called_once_with(self.mock_couriermenu)
        mock_get_items.assert_called_once_with(self.mock_productmenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_name, 'Testname2')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_address, 'Testplanet')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_phone, '1122334455')
        self.assertEqual(self.test_ordermenu.orders[1].courier, 55)
        self.assertEqual(self.test_ordermenu.orders[1].items, '1,3,2')
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Testname2\'s order',))

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_update3(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when address is blank'''
        mock_input.side_effect = ['Test4', '', '1122334455']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_update(
            1, self.mock_productmenu, self.mock_couriermenu)
        mock_get_courier.assert_called_once_with(self.mock_couriermenu)
        mock_get_items.assert_called_once_with(self.mock_productmenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_name, 'Test4')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_address, 'Testcity')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_phone, '1122334455')
        self.assertEqual(self.test_ordermenu.orders[1].courier, 55)
        self.assertEqual(self.test_ordermenu.orders[1].items, '1,3,2')
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Test4\'s order',))

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_update4(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when phone is blank'''
        mock_input.side_effect = ['Test4', 'Testplanet', '']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_update(
            1, self.mock_productmenu, self.mock_couriermenu)
        mock_get_courier.assert_called_once_with(self.mock_couriermenu)
        mock_get_items.assert_called_once_with(self.mock_productmenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_name, 'Test4')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_address, 'Testplanet')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_phone, '6601000080')
        self.assertEqual(self.test_ordermenu.orders[1].courier, 55)
        self.assertEqual(self.test_ordermenu.orders[1].items, '1,3,2')
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Test4\'s order',))

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_update5(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when courier ID is blank'''
        mock_input.side_effect = ['Test4', 'Testplanet', '1122334455']
        mock_get_courier.return_value = 0
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_update(
            1, self.mock_productmenu, self.mock_couriermenu)
        mock_get_courier.assert_called_once_with(self.mock_couriermenu)
        mock_get_items.assert_called_once_with(self.mock_productmenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_name, 'Test4')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_address, 'Testplanet')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_phone, '1122334455')
        self.assertEqual(self.test_ordermenu.orders[1].courier, 7)
        self.assertEqual(self.test_ordermenu.orders[1].items, '1,3,2')
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Test4\'s order',))

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_update6(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when item IDs are blank'''
        mock_input.side_effect = ['Test4', 'Testplanet', '1122334455']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = ''

        self.test_ordermenu.set_order_update(
            1, self.mock_productmenu, self.mock_couriermenu)
        mock_get_courier.assert_called_once_with(self.mock_couriermenu)
        mock_get_items.assert_called_once_with(self.mock_productmenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_name, 'Test4')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_address, 'Testplanet')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_phone, '1122334455')
        self.assertEqual(self.test_ordermenu.orders[1].courier, 55)
        self.assertEqual(self.test_ordermenu.orders[1].items, '5')
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Test4\'s order',))

    @patch('ordermenu.datalogger')
    @patch('ordermenu.Order_menu.set_order_get_items')
    @patch('ordermenu.Order_menu.set_order_get_courier')
    @patch('builtins.input')
    def test_set_order_update7(
            self, mock_input: MagicMock, mock_get_courier: MagicMock,
            mock_get_items: MagicMock, mock_logger: MagicMock):
        '''Test when phone is invalid'''
        mock_input.side_effect = ['Test4', 'Testplanet', 'foobar']
        mock_get_courier.return_value = 55
        mock_get_items.return_value = '1,3,2'

        self.test_ordermenu.set_order_update(
            1, self.mock_productmenu, self.mock_couriermenu)
        mock_get_courier.assert_called_once_with(self.mock_couriermenu)
        mock_get_items.assert_called_once_with(self.mock_productmenu)

        self.assertEqual(len(self.test_ordermenu.orders), 3)
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_name, 'Test4')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_address, 'Testplanet')
        self.assertEqual(
            self.test_ordermenu.orders[1].customer_phone, '6601000080')
        self.assertEqual(self.test_ordermenu.orders[1].courier, 55)
        self.assertEqual(self.test_ordermenu.orders[1].items, '1,3,2')
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Test4\'s order',))

    @patch('ordermenu.datalogger')
    @patch('builtins.input')
    def test_set_order_update_status(
            self, mock_input: MagicMock, mock_logger: MagicMock):
        mock_input.return_value = '1'
        self.test_ordermenu.set_order_update_status(1)
        self.assertEqual(
            self.test_ordermenu.orders[1].status, 'Preparing')
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Testname2\'s order',))

        mock_input.return_value = '2'
        self.test_ordermenu.set_order_update_status(1)
        self.assertEqual(
            self.test_ordermenu.orders[1].status, 'Awaiting pickup')
        self.assertEqual(
            mock_logger.mock_calls[1][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[1].args, ('Testname2\'s order',))

        mock_input.return_value = '3'
        self.test_ordermenu.set_order_update_status(1)
        self.assertEqual(
            self.test_ordermenu.orders[1].status, 'Out for delivery')
        self.assertEqual(
            mock_logger.mock_calls[2][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[2].args, ('Testname2\'s order',))

        mock_input.return_value = '4'
        self.test_ordermenu.set_order_update_status(1)
        self.assertEqual(
            self.test_ordermenu.orders[1].status, 'Delivered')
        self.assertEqual(
            mock_logger.mock_calls[3][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[3].args, ('Testname2\'s order',))

        mock_input.return_value = 'foobar'
        self.test_ordermenu.set_order_update_status(1)
        self.assertEqual(
            self.test_ordermenu.orders[1].status, 'Delivered')
        self.assertEqual(
            mock_logger.mock_calls[4][0], 'log_update')
        self.assertEqual(
            mock_logger.mock_calls[4].args, ('Testname2\'s order',))

    @patch('ordermenu.datalogger')
    def test_set_order_remove(
            self, mock_logger: MagicMock):
        removed_order = self.test_ordermenu.orders[1]

        result = self.test_ordermenu.set_order_remove(1)
        self.assertEqual(
            self.mock_database.mock_calls[1][0], '().remove_order')
        self.assertEqual(
            self.mock_database.mock_calls[1].args, (removed_order,))
        self.assertEqual(len(self.test_ordermenu.orders), 2)
        self.assertEqual(result, 'Testname2\'s order')
        self.assertEqual(
            mock_logger.mock_calls[0][0], 'log_remove')
        self.assertEqual(
            mock_logger.mock_calls[0].args, ('Testname2\'s order',))


if __name__ == '__main__':
    unittest.main()
