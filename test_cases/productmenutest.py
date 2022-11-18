"""_summary_
"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from productmenu import Product_menu
from productclass import Product


class TestMainMenu(unittest.TestCase):

    @patch('productmenu.Product_menu.load_products_database')
    @patch('productclass.Product')
    @patch('database.Database')
    def setUp(
            self, mock_database: MagicMock, mock_product: MagicMock,
            mock_load_database: MagicMock):
        self.testmenu = Product_menu()

    def test_setUp(
            self):
        pass


if __name__ == '__main__':
    unittest.main()
