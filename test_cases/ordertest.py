# This code doesn't really do anything right now.

import unittest


class TestOrderAttributes(unittest.TestCase):

    def test_name(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_address(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_phone(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_status(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_get_order(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
