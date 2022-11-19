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
            Courier('Test1', 'phone1'), Courier('Test2', 'phone2'),
            Courier('Test3', 'phone3')]

    def test_setUp(
            self):
        self.database_load.assert_called()


if __name__ == '__main__':
    unittest.main()
