import unittest

from business.menu_items import MenuItems


class TestUserClass(unittest.TestCase):
    def test_new_menu_item(self):
        m1 = MenuItems()
        self.assertEqual(m1.get_id(), None)
        self.assertEqual(m1.get_name(), None)
        self.assertEqual(m1.get_description(), None)
        self.assertEqual(m1.get_price(), None)
        self.assertEqual(m1.get_category(), None)

        # print(s1.to_string())

        m1.set_name('Pizza')
        self.assertEqual(m1.get_name(), 'Pizza')
        m1.set_price(15)
        self.assertEqual(m1.get_price(), 15)
        m1.set_description('Margharita pizza')
        self.assertEqual(m1.get_description(), 'Margharita pizza')
        m1.set_category('Main Course')
        self.assertEqual(m1.get_category(), 'Main Course')

        # print(s1.to_string())

    def test_build_menu_item(self):
        m1 = MenuItems.build('Pasta', 'Main Course', 25, 'rottini with meatballs')
        print(m1.to_string())

        self.assertEqual(m1.get_name(), 'Pasta')
        self.assertEqual(m1.get_price(), 25)
        self.assertEqual(m1.get_category(), 'Main Course')
        self.assertEqual(m1.get_description(), 'rottini with meatballs')
