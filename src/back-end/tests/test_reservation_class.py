import unittest

from business.reservation import Reservation


class TestUserClass(unittest.TestCase):
    def test_getting_reservation(self):
        r1 = Reservation()
        self.assertEqual(r1.get_id(), None)
        self.assertEqual(r1.get_timestamp(), None)
        self.assertEqual(r1.get_customer_name(), None)
        self.assertEqual(r1.get_customer_id(), None)
        self.assertEqual(r1.get_seat_count(), None)
        self.assertEqual(r1.get_table_id(), None)
        self.assertEqual(r1.get_for_date(), None)
        self.assertEqual(r1.get_for_how_long(), None)
        self.assertEqual(r1.get_status(), None)
        self.assertEqual(r1.get_latest_comment(), None)
        self.assertEqual(r1.get_waiter_id(), None)
        self.assertEqual(r1.get_reservation_type(), None)
        self.assertEqual(r1.get_total_price(), None)
        self.assertEqual(r1.get_tip_percent(), None)
        # print(r1.to_string())

    def test_adding_new_reservation(self):
        r1 = Reservation()
        self.assertEqual(r1.get_id(), None)
        r1.set_timestamp('2023/05/21')
        self.assertEqual(r1.get_timestamp(), '2023/05/21')
        r1.set_customer_name('Tina')
        self.assertEqual(r1.get_customer_name(), 'Tina')
        r1.set_customer_id(12)
        self.assertEqual(r1.get_customer_id(), 12)
        r1.set_seat_count(6)
        self.assertEqual(r1.get_seat_count(), 6)
        r1.set_table_id(4)
        self.assertEqual(r1.get_table_id(), 4)
        r1.set_for_date('2021/05/28')
        self.assertEqual(r1.get_for_date(), '2021/05/28')
        r1.set_for_how_long(2)
        self.assertEqual(r1.get_for_how_long(), 2)
        r1.set_status('reserved')
        self.assertEqual(r1.get_status(), 'reserved')
        r1.set_latest_comment('no comment')
        self.assertEqual(r1.get_latest_comment(), 'no comment')
        r1.set_waiter_id(15)
        self.assertEqual(r1.get_waiter_id(), 15)
        r1.set_reservation_type('phone')
        self.assertEqual(r1.get_reservation_type(), 'phone')
        r1.set_total_price(76)
        self.assertEqual(r1.get_total_price(), 76)
        r1.set_tip_percent(10)
        self.assertEqual(r1.get_tip_percent(), 10)
        # print(r1.to_string()

        r1.add()
        self.assertTrue(r1.get_id() is not None)
        self.assertTrue(r1.get_id() >= 0)

    def test_select_all_reservation(self):
        reservations = Reservation.select_all()
        self.assertTrue(len(reservations) >= 0)

    def test_load_and_update_reservation(self):
        data = Reservation.select_all()
        if len(data) > 0:
            sample_id = data[1]['id']
            r1 = Reservation()
            r1.load(sample_id)
            old_total = r1.get_total_price()
            r1.set_total_price(old_total * 1.02)
            self.assertTrue(r1.update())
            self.assertTrue(old_total != r1.get_total_price())

    def test_add_order_item(self):
        data = Reservation.select_all()
        if len(data) > 0:
            sample_id = data[1]['id']
            r1 = Reservation()
            r1.load(sample_id)
            # print(r1.to_string())

            self.assertTrue(r1.add_order_item('Pizza', 2))
            self.assertTrue(r1.add_order_item('Diet Coke', 2))
            self.assertTrue(r1.add_order_item('Salad', 1))

    def test_select_all_order_items(self):
        data = Reservation.select_all()
        if len(data) > 0:
            sample_id = data[1]['id']
            r1 = Reservation()
            r1.load(sample_id)
            order_items = r1.get_all_order_items()
            self.assertTrue(len(order_items) >= 0)
