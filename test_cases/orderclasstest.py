"""Author: Nathan \n
Unit tests for orderclass.py
"""

import unittest

import orderclass as orderclass


class TestOrderClass(unittest.TestCase):

    def setUp(self) -> None:
        self.test_order = orderclass.Order('Johnny', 'Everytown', '0800001066')

    def test_setUp(self):
        self.assertEqual(self.test_order.id, 0)
        self.assertEqual(self.test_order.customer_name, 'Johnny')
        self.assertEqual(self.test_order.customer_address, 'Everytown')
        self.assertEqual(self.test_order.customer_phone, '0800001066')
        self.assertEqual(self.test_order.courier, None)
        self.assertEqual(self.test_order.statuscode, 1)
        self.assertEqual(self.test_order.status, 'Preparing')
        self.assertEqual(self.test_order.items, '')

    def test_set_attributes(self):
        self.test_order.set_order_name('Jimmy')
        self.test_order.set_order_address('Notown')
        self.test_order.set_order_phone('6601000080')

        self.assertEqual(self.test_order.customer_name, 'Jimmy')
        self.assertEqual(self.test_order.customer_address, 'Notown')
        self.assertEqual(self.test_order.customer_phone, '6601000080')

    def test_set_courier(self):
        self.test_order.set_courier('')
        self.assertEqual(self.test_order.courier, None)

        self.test_order.set_courier('5')
        self.assertEqual(self.test_order.courier, 5)

        self.test_order.set_courier(5)
        self.assertEqual(self.test_order.courier, 5)

    def test_get_courier(self):
        self.assertEqual(self.test_order.get_courier(), 'None')

        self.test_order.set_courier('5')
        self.assertEqual(self.test_order.get_courier(), 5)

    def test_status_update(self):
        self.test_order.set_order_status('1')
        self.assertEqual(self.test_order.statuscode, 1)
        self.assertEqual(self.test_order.status, 'Preparing')

        self.test_order.set_order_status('2')
        self.assertEqual(self.test_order.statuscode, 2)
        self.assertEqual(self.test_order.status, 'Awaiting pickup')

        self.test_order.set_order_status('3')
        self.assertEqual(self.test_order.statuscode, 3)
        self.assertEqual(self.test_order.status, 'Out for delivery')

        self.test_order.set_order_status('4')
        self.assertEqual(self.test_order.statuscode, 4)
        self.assertEqual(self.test_order.status, 'Delivered')

    def test_set_items(self):
        self.test_order.set_items('4,5,2')
        self.assertEqual(self.test_order.items, '4,5,2')

    def test_get_items(self):
        self.assertEqual(self.test_order.get_items(), 'None')

        self.test_order.set_items('4,5,2')
        self.assertEqual(self.test_order.get_items(), '4,5,2')

    def test_get_order(self):
        self.assertEqual(self.test_order.get_order(),
                         {'id': 0,
                          'customer_name': 'Johnny',
                          'customer_address': 'Everytown',
                          'customer_phone': '0800001066',
                          'courier': None,
                          'statuscode': 1,
                          'items': ''})


if __name__ == '__main__':
    unittest.main()
