import unittest

import string
import random

from business.user import User


class TestUserClass(unittest.TestCase):
    def test_new_user(self):
        u1 = User()
        self.assertEqual(u1.get_id(), None)
        self.assertEqual(u1.get_name(), None)

        u1.set_name('tina')
        self.assertEqual(u1.get_name(), 'tina')

        u2 = User()
        self.assertEqual(u2.get_name(), None)
        u2.set_name('mina')
        self.assertEqual(u2.get_name(), 'mina')

    def test_build_user(self):
        u1 = User.build("tina", "tina@tina.com", "123", "2020-10-10")
        self.assertEqual(u1.get_email(), 'tina@tina.com')
        self.assertEqual(u1.get_password(), '123')

    def test_add_user(self):
        u1 = User.build("chuck", "chuck@buymore.com", "123", "2020-10-10")
        self.assertEqual(u1.get_email(), 'chuck@buymore.com')
        self.assertEqual(u1.get_password(), '123')
        self.assertTrue(u1.add())

        self.assertTrue(u1.get_id() is not None)
        self.assertTrue(u1.get_id() >= 0)
        print(u1.get_id())

    def test_load_user(self):
        data = User.select_all_users()

        if len(data) > 0:
            u1 = User()
            self.assertTrue(u1.get_id() is None)

            sample_id = data[0][0]
            u1.load(sample_id)
            self.assertTrue(u1.get_id() == sample_id)

            letters = string.ascii_lowercase
            new_pass_word = ''.join(random.choice(letters) for i in range(10))
            u1.set_password(new_pass_word)
            self.assertTrue(u1.update())

    def test_delete_user(self):
        u1 = User.build("kamran", "kamran@tina.com", "123", "2020-10-10")
        self.assertTrue(u1.add())
        self.assertTrue(User.delete(u1.get_id()))

    def test_load_user_by_email(self):
        u1 = User()
        self.assertTrue(u1.get_id() is None)

        u1.load_by_email("chuck@buymore.com")
        self.assertTrue(u1.get_email(), "chuck@buymore.com")
        print(u1.to_string())
