"""Author: Nathan \n
Unit tests for couriermenu.py
"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from couriermenu import Courier_menu
from courierclass import Courier


class TestCourierMenu(unittest.TestCase):

    @patch('couriermenu.Courier_menu.load_couriers_database')
    @patch('couriermenu.Database')
    def setUp(
            self, mock_database: MagicMock, mock_database_load: MagicMock):
        self.testmenu = Courier_menu()
        self.mock_database = mock_database
        mock_database.reset_mock()
        self.database_load = mock_database_load
        self.testmenu.couriers.clear()
        self.testmenu.couriers = [
            Courier('Test1', '0800001066'), Courier('Test2', '6601000080'),
            Courier('Test3', '0080006610')]

    def test_setUp(
            self):
        self.database_load.assert_called()

    @patch('couriermenu.sleep')
    @patch('builtins.print')
    def test_list_couriers(
            self, mock_print: MagicMock, mock_sleep: MagicMock):
        list_length = self.testmenu.list_couriers()

        self.assertEqual(list_length, 3)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(
            mock_print.mock_calls[0][1][0],
            'Courier No.0:'
            '\n\tCourier name: Test1'
            '\n\tCourier phone: 0800001066')
        self.assertEqual(
            mock_print.mock_calls[1][1][0],
            'Courier No.0:'
            '\n\tCourier name: Test2'
            '\n\tCourier phone: 6601000080')
        self.assertEqual(
            mock_print.mock_calls[2][1][0],
            'Courier No.0:'
            '\n\tCourier name: Test3'
            '\n\tCourier phone: 0080006610')

    def test_load_couriers_database(
            self):
        self.mock_database.return_value.load_couriers.return_value = [
            {'id': 4, 'name': 'dTest', 'phone': '0900221055'},
            {'id': 27, 'name': 'dTest2', 'phone': '5501220090'}]

        self.testmenu.load_couriers_database()
        self.assertEqual(self.testmenu.couriers[0].id, 4)
        self.assertEqual(self.testmenu.couriers[0].name, 'dTest')
        self.assertEqual(self.testmenu.couriers[0].phone, '0900221055')
        self.assertEqual(self.testmenu.couriers[1].id, 27)
        self.assertEqual(self.testmenu.couriers[1].name, 'dTest2')
        self.assertEqual(self.testmenu.couriers[1].phone, '5501220090')

    def test_save_couriers_database(
            self):
        self.testmenu.save_couriers_database()
        self.assertEqual(
            self.mock_database.mock_calls[0][0], '().save_couriers')
        self.assertEqual(
            self.mock_database.mock_calls[0][1][0], self.testmenu.couriers)

    @patch('builtins.input')
    def test_set_courier_create(
            self, mock_input: MagicMock):
        mock_input.side_effect = ['Test4', '0900221055']
        self.mock_database.return_value.insert_courier.return_value = 50

        self.testmenu.set_courier_create()
        self.assertEqual(self.testmenu.couriers[3].id, 50)
        self.assertEqual(self.testmenu.couriers[3].name, 'Test4')
        self.assertEqual(self.testmenu.couriers[3].phone, '0900221055')

    @patch('builtins.input')
    def test_set_courier_update(
            self, mock_input: MagicMock):
        mock_input.side_effect = ['Test4', '0900221055']

        self.testmenu.set_courier_update(1)
        self.assertEqual(self.testmenu.couriers[1].name, 'Test4')
        self.assertEqual(self.testmenu.couriers[1].phone, '0900221055')

    @patch('builtins.input')
    def test_set_courier_update2(
            self, mock_input: MagicMock):
        mock_input.side_effect = ['', '0900221056']
        self.testmenu.set_courier_update(1)
        self.assertEqual(self.testmenu.couriers[1].name, 'Test2')
        self.assertEqual(self.testmenu.couriers[1].phone, '0900221056')

    @patch('builtins.input')
    def test_set_courier_update3(
            self, mock_input: MagicMock):
        mock_input.side_effect = ['Test5', '']
        self.testmenu.set_courier_update(1)
        self.assertEqual(self.testmenu.couriers[1].name, 'Test5')
        self.assertEqual(self.testmenu.couriers[1].phone, '6601000080')

    @patch('builtins.input')
    def test_set_courier_update4(
            self, mock_input: MagicMock):
        mock_input.side_effect = ['', '']
        self.testmenu.set_courier_update(1)
        self.assertEqual(self.testmenu.couriers[1].name, 'Test2')
        self.assertEqual(self.testmenu.couriers[1].phone, '6601000080')

    @patch('builtins.input')
    def test_set_courier_update5(
            self, mock_input: MagicMock):
        mock_input.side_effect = ['Test5', 'Test6']
        self.testmenu.set_courier_update(1)
        # self.assertRaises(ValueError)
        self.assertEqual(self.testmenu.couriers[1].name, 'Test5')
        self.assertEqual(self.testmenu.couriers[1].phone, '6601000080')

    def test_set_courier_remove(
            self):
        removed_courier = self.testmenu.couriers[1]

        result = self.testmenu.set_courier_remove(1)
        self.assertEqual(
            self.mock_database.mock_calls[0][0], '().remove_courier')
        self.assertEqual(
            self.mock_database.mock_calls[0].args, (removed_courier,))
        self.assertEqual(len(self.testmenu.couriers), 2)
        self.assertEqual(result, 'Test2')


if __name__ == '__main__':
    unittest.main()
