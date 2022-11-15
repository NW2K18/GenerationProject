"""Author: Nathan \n
Unit tests for courierclass.py
"""

import unittest

import courierclass as courierclass


class TestCourierObject(unittest.TestCase):

    def setUp(self) -> None:
        self.test_courier = courierclass.Courier('Nate', '0800001066')

    def test_create_product(self):
        self.assertEqual(self.test_courier.name, 'Nate')
        self.assertEqual(self.test_courier.phone, '0800001066')

    def test_set_attributes(self):
        self.test_courier.set_courier_name('Saul')
        self.test_courier.set_courier_phone('6601000080')

        self.assertEqual(self.test_courier.name, 'Saul')
        self.assertEqual(self.test_courier.phone, '6601000080')

    def test_get_courier(self):
        self.assertEqual(self.test_courier.get_courier(),
                         {'name': 'Nate',
                         'phone': '0800001066'})


if __name__ == '__main__':
    unittest.main()
