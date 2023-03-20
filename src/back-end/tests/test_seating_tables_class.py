import unittest

from business.seating_tables import SeatingTables


class TestUserClass(unittest.TestCase):
    def test_new_seat_count(self):
        s1 = SeatingTables()
        self.assertEqual(s1.get_id(), None)
        self.assertEqual(s1.get_seat_count(), None)
        self.assertEqual(s1.get_available(), None)

        print(s1.to_string())

        s2 = SeatingTables()
        s2.set_seat_count(4)
        self.assertEqual(s2.get_seat_count(), 4)

        s2.set_available('False')
        self.assertEqual(s2.get_available(),'False')
        print(s2.to_string())