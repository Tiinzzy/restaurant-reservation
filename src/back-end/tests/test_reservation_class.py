import unittest

from business.reservation import Reservation


class TestUserClass(unittest.TestCase):
    def test_new_reservation(self):
        r1 = Reservation()
