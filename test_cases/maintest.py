# Author: Nathan
# Unit tests for main.py

import unittest

import main


class TestMainMenu(unittest.TestCase):

    def test_true(self):
        testmenu = main.Menu()
        # testmenu.main()
        assert True


if __name__ == '__main__':
    unittest.main()
