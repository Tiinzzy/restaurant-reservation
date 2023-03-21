import unittest

from business.reservation import Reservation


class TestUserClass(unittest.TestCase):
    def test_new_reservation(self):
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
        print(r1.to_string())
