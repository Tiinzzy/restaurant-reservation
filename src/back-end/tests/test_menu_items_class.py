import unittest

from business.menu_items import MenuItems


class TestUserClass(unittest.TestCase):
    def test_new_menu_item(self):
        s1 = MenuItems()
        self.assertEqual(s1.get_id(), None)
        self.assertEqual(s1.get_name(), None)
        self.assertEqual(s1.get_description(), None)
        self.assertEqual(s1.get_price(), None)
        self.assertEqual(s1.get_category(), None)

        print(s1.to_string())

        s1.set_name('Pizza')
        self.assertEqual(s1.get_name(), 'Pizza')
        s1.set_price(15)
        self.assertEqual(s1.get_price(), 15)
        s1.set_description('Margharita pizza')
        self.assertEqual(s1.get_description(), 'Margharita pizza')
        s1.set_category('Main Course')
        self.assertEqual(s1.get_category(), 'Main Course')

        print(s1.to_string())
