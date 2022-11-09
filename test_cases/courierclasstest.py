# Author: Nathan
# Unit tests for courierclass.py

import unittest

import courierclass as courierclass


class TestCourierAttributes(unittest.TestCase):
    def test_create_product(self):
        test_courier = courierclass.Courier('Nate', '0800001066')
        self.assertEqual(test_courier.name, 'Nate')
        self.assertEqual(test_courier.phone, '0800001066')

    def test_set_attributes(self):
        test_courier = courierclass.Courier('Nate', '0800001066')

        test_courier.set_courier_name('Saul')
        test_courier.set_courier_phone('6601000080')

        self.assertEqual(test_courier.name, 'Saul')
        self.assertEqual(test_courier.phone, '6601000080')

    def test_get_courier(self):
        test_courier = courierclass.Courier('Nate', '0800001066')
        self.assertEqual(test_courier.get_courier(),
                         {'name': 'Nate',
                         'phone': '0800001066'})


if __name__ == '__main__':
    unittest.main()
