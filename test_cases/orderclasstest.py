# Author: Nathan
# Unit tests for orderclass.py

import unittest

import orderclass


class TestOrderAttributes(unittest.TestCase):

    def test_create_order(self):
        test_order = orderclass.Order('Johnny', 'Everytown', '0800001066')
        self.assertEqual(test_order.customer_name, 'Johnny')
        self.assertEqual(test_order.customer_address, 'Everytown')
        self.assertEqual(test_order.customer_phone, '0800001066')
        self.assertEqual(test_order.courier, None)
        self.assertEqual(test_order.status, 'Preparing')
        self.assertEqual(test_order.items, '')

    def test_set_attributes(self):
        test_order = orderclass.Order('Johnny', 'Everytown', '0800001066')

        test_order.set_order_name('Jimmy')
        test_order.set_order_address('Notown')
        test_order.set_order_phone('6601000080')

        self.assertEqual(test_order.customer_name, 'Jimmy')
        self.assertEqual(test_order.customer_address, 'Notown')
        self.assertEqual(test_order.customer_phone, '6601000080')

    def test_set_courier(self):
        test_order = orderclass.Order('Johnny', 'Everytown', '0800001066')

        test_order.set_courier(5)
        self.assertEqual(test_order.courier, 5)

    def test_get_courier(self):
        test_order = orderclass.Order('Johnny', 'Everytown', '0800001066')
        self.assertEqual(test_order.get_courier(), 'None')

        test_order.set_courier(5)
        self.assertEqual(test_order.get_courier(), 5)

    def test_status_update(self):
        test_order0 = orderclass.Order('Johnny', 'Everytown', '0800001066')
        test_order1 = orderclass.Order('Johnny', 'Everytown', '0800001066')
        test_order2 = orderclass.Order('Johnny', 'Everytown', '0800001066')
        test_order3 = orderclass.Order('Johnny', 'Everytown', '0800001066')

        test_order0.set_order_status('0')
        test_order1.set_order_status('1')
        test_order2.set_order_status('2')
        test_order3.set_order_status('3')

        self.assertEqual(test_order0.status, 'Preparing')
        self.assertEqual(test_order1.status, 'Awaiting pickup')
        self.assertEqual(test_order2.status, 'Out for delivery')
        self.assertEqual(test_order3.status, 'Delivered')

    def test_set_items(self):
        test_order = orderclass.Order('Johnny', 'Everytown', '0800001066')

        test_order.set_items('4,5,2')
        self.assertEqual(test_order.items, '4,5,2')

    def test_get_items(self):
        test_order = orderclass.Order('Johnny', 'Everytown', '0800001066')
        self.assertEqual(test_order.get_items(), 'None')

        test_order.set_items('4,5,2')
        self.assertEqual(test_order.get_items(), '4,5,2')

    def test_get_order(self):
        test_order = orderclass.Order('Johnny', 'Everytown', '0800001066')
        self.assertEqual(test_order.get_order(),
                         {'customer_name': 'Johnny',
                          'customer_address': 'Everytown',
                          'customer_phone': '0800001066',
                          'courier': None,
                          'status': 'Preparing',
                          'items': ''})


if __name__ == '__main__':
    unittest.main()
