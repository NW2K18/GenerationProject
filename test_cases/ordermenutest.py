# Author: Nathan
# Unit tests for orderclass.py

import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from ordermenu import Order_menu
from orderclass import Order


class TestOrderMenu(unittest.TestCase):

    @patch('ordermenu.Order_menu.load_orders')
    def setUp(self, mock_load):
        self.test_ordermenu = Order_menu()
        self.test_ordermenu.orders.clear()
        self.test_ordermenu.orders.append(Order('Testname', 'Testtown',
                                          '0800001066'))
        self.test_ordermenu.orders.append(Order('Testname2', 'Testcity',
                                          '6601000080'))
        self.test_ordermenu.orders.append(Order('Testname3', 'Testcountry',
                                          '1066080000'))

    @patch('ordermenu.Order_menu.load_orders')
    def test_same_type(self, mock_load: MagicMock):
        test_ordermenu2 = Order_menu()
        self.assertEqual(type(self.test_ordermenu), type(test_ordermenu2))
        mock_load.assert_called_once()

    @patch('ordermenu.sleep')
    @patch('builtins.print')
    def test_list_orders(self, mock_print: MagicMock, mock_sleep: MagicMock):
        self.assertEqual(
            self.test_ordermenu.list_orders(self.test_ordermenu.orders), 3)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 3)

        self.test_ordermenu.orders.pop()
        self.assertEqual(
            self.test_ordermenu.list_orders(self.test_ordermenu.orders), 2)

        self.test_ordermenu.orders.pop()
        self.test_ordermenu.orders.pop()
        self.assertEqual(
            self.test_ordermenu.list_orders(self.test_ordermenu.orders), 0)


if __name__ == '__main__':
    unittest.main()
