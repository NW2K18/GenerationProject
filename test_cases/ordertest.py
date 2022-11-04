# This code doesn't really do anything right now.

import unittest

import orderclass


class TestOrderAttributes(unittest.TestCase):

    def test_false(self):
        assert False

    def test_create_order(self):
        test_order = orderclass.Order('Johnny', 'Everytown', '0800001066')
        self.assertEqual(test_order.name, 'Johnny')
        self.assertEqual(test_order.address, 'Everytown')
        self.assertEqual(test_order.phone, '0800001066')
        self.assertEqual(test_order.status, 'Preparing')

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

    def test_get_order(self):
        test_order = orderclass.Order('Johnny', 'Everytown', '0800001066')
        self.assertEqual(test_order.get_order(),
                         {'customer_name': 'Johnny',
                          'customer_address': 'Everytown',
                          'customer_phone': '0800001066',
                          'status': 'Preparing'})


if __name__ == '__main__':
    unittest.main()
