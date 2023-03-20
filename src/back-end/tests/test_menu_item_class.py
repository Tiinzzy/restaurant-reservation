import unittest

from business.menu_item import MenuItem


class TestUserClass(unittest.TestCase):
    def test_new_menu_item(self):
        m1 = MenuItem()
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
        m1 = MenuItem.build('Pasta', 'Main Course', 25, 'rottini with meatballs')
        # print(m1.to_string())

        self.assertEqual(m1.get_name(), 'Pasta')
        self.assertEqual(m1.get_price(), 25)
        self.assertEqual(m1.get_category(), 'Main Course')
        self.assertEqual(m1.get_description(), 'rottini with meatballs')

    def test_add_menu_item(self):
        m1 = MenuItem.build('Pasta', 'Main Course', 25, 'rottini with meatballs')
        result = m1.add()
        self.assertTrue(result)
        self.assertTrue(m1.get_id() is not None)
        self.assertTrue(m1.get_id() >= 0)

        m2 = MenuItem()
        m2.set_name('Pizza')
        m2.set_price(15)
        m2.set_category('Main Course')
        m2.set_description('Margharita pizza')
        result = m2.add()
        self.assertTrue(result)
        self.assertTrue(m2.get_id() is not None)
        self.assertTrue(m2.get_id() >= 0)

    def test_delete_menu_item(self):
        m1 = MenuItem.build('Fries', 'Entrees', 10, 'potato fries')
        result = m1.add()
        self.assertTrue(result)
        result = m1.delete()
        self.assertTrue(result)

        m2 = MenuItem()
        m2.set_name('Salad')
        m2.set_price(14)
        m2.set_category('Entrees')
        m2.set_description('caesar salad')
        result = m2.add()
        self.assertTrue(result)

    def test_select_all_menu_items(self):
        menu_items = MenuItem.select_all_menu_items()
        self.assertTrue(len(menu_items) >= 0)

    def test_select_menu_item(self):
        m1 = MenuItem.build('Fries', 'Entrees', 10, 'potato fries')
        result = m1.add()
        self.assertTrue(result)
        item_id = m1.get_id()
        self.assertTrue(item_id == m1.get_id())
        result = m1.load(item_id)
        self.assertTrue(result)
        self.assertEqual(m1.get_id(), item_id)
        self.assertEqual(m1.get_name(), 'Fries')
        self.assertEqual(m1.get_category(), 'Entrees')
        self.assertEqual(m1.get_price(), 10)
        self.assertEqual(m1.get_description(), 'potato fries')

    def test_update_menu_item(self):
        data = MenuItem.select_all_menu_items()
        if len(data) > 0:
            sample_id = data[0]['id']
            m1 = MenuItem()
            m1.load(sample_id)
            old_price = m1.get_price()
            m1.set_price(old_price * 1.01)
            self.assertTrue(m1.update())
            self.assertTrue(old_price != m1.get_price())
