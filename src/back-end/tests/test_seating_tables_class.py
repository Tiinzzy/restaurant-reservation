import unittest

from business.seating_tables import SeatingTables


class TestUserClass(unittest.TestCase):
    def test_new_seat_count(self):
        s1 = SeatingTables()
        self.assertEqual(s1.get_id(), None)
        self.assertEqual(s1.get_seat_count(), None)
        self.assertEqual(s1.get_available(), None)

        # print(s1.to_string())

        s2 = SeatingTables()
        s2.set_seat_count(4)
        self.assertEqual(s2.get_seat_count(), 4)

        s2.set_available('False')
        self.assertEqual(s2.get_available(), 'False')
        # print(s2.to_string())

    def test_build_seating(self):
        s1 = SeatingTables.build(2, 'True')
        self.assertEqual(s1.get_seat_count(), 2)
        self.assertEqual(s1.get_available(), 'True')

        # print(s1.to_string())

    def test_add_seating_tables(self):
        s1 = SeatingTables.build(4, 'False')
        self.assertEqual(s1.get_seat_count(), 4)
        self.assertEqual(s1.get_available(), 'False')

        s1.add()
        self.assertTrue(s1.get_id() is not None)
        self.assertTrue(s1.get_id() >= 0)

        # print(s1.to_string())
