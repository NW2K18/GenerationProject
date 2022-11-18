"""Author: Nathan \n
Unit tests for productmenu.py
"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from couriermenu import Courier_menu
from courierclass import Courier


class TestCourierMenu(unittest.TestCase):

    @patch('couriermenu.Courier_menu.load_couriers_database')
    @patch('database.Database')
    def setUp(
            self, mock_database: MagicMock, mock_load_database: MagicMock):
        self.testmenu = Courier_menu()
        self.testdatabase = mock_database
        self.load_on_startup = mock_load_database
        self.testmenu.couriers.clear()
        self.testmenu.couriers = [
            Courier('Test1', 'phone1'), Courier('Test2', 'phone2'),
            Courier('Test3', 'phone3')]

    def test_setUp(
            self):
        self.load_on_startup.assert_called()


if __name__ == '__main__':
    unittest.main()
