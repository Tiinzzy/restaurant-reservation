import unittest

from business.seating_table import SeatingTable


class TestUserClass(unittest.TestCase):
    def test_new_seat_count(self):
        s1 = SeatingTable()
        self.assertEqual(s1.get_id(), None)
        self.assertEqual(s1.get_seat_count(), None)
        self.assertEqual(s1.get_available(), None)

        s2 = SeatingTable()
        s2.set_seat_count(4)
        self.assertEqual(s2.get_seat_count(), 4)

        s2.set_available(False)
        self.assertEqual(s2.get_available(), False)

    def test_build_seating(self):
        s1 = SeatingTable.build(2, True)
        self.assertEqual(s1.get_seat_count(), 2)
        self.assertEqual(s1.get_available(), True)

    def test_add_seating_tables(self):
        s1 = SeatingTable.build(35, False)
        self.assertEqual(s1.get_seat_count(), 35)
        self.assertEqual(s1.get_available(), False)

        self.assertTrue(s1.add())
        self.assertTrue(s1.get_id() is not None)
        self.assertTrue(s1.get_id() >= 0)

    def test_select_available_seats(self):
        s1 = SeatingTable.select_available_seats(2)
        self.assertTrue(len(s1) >= 0)

    def test_updating_seating_tables(self):
        result = SeatingTable.select_all_seating_tables()
        if len(result) > 0:
            sample_id = result[0]['id']
            s1 = SeatingTable()
            s1.load(sample_id)
            s1.set_available(not s1.get_available())
            s1.set_seat_count(2 + (s1.get_seat_count() + 1) % 5)
            result = s1.update()
            self.assertTrue(result)

    def test_delete_seating_table(self):
        s1 = SeatingTable.build(4, True)
        s1.add()
        result = s1.delete()
        self.assertTrue(result)

    def test_select_all_seating_tables(self):
        result = SeatingTable.select_all_seating_tables()
        self.assertTrue(len(result) >= 0)
