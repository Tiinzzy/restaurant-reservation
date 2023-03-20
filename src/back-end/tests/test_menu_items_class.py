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
        # print(m1.to_string())

        self.assertEqual(m1.get_name(), 'Pasta')
        self.assertEqual(m1.get_price(), 25)
        self.assertEqual(m1.get_category(), 'Main Course')
        self.assertEqual(m1.get_description(), 'rottini with meatballs')

    def test_add_menu_item(self):
        m1 = MenuItems.build('Pasta', 'Main Course', 25, 'rottini with meatballs')
        result = m1.add()
        self.assertTrue(result)
        self.assertTrue(m1.get_id() is not None)
        self.assertTrue(m1.get_id() >= 0)

        m2 = MenuItems()
        m2.set_name('Pizza')
        m2.set_price(15)
        m2.set_category('Main Course')
        m2.set_description('Margharita pizza')
        result = m2.add()
        self.assertTrue(result)
        self.assertTrue(m2.get_id() is not None)
        self.assertTrue(m2.get_id() >= 0)

    def test_delete_menu_item(self):
        m1 = MenuItems.build('Fries', 'Entrees', 10, 'potato fries')
        result = m1.add()
        self.assertTrue(result)
        result = m1.delete()
        self.assertTrue(result)

        m2 = MenuItems()
        m2.set_name('Salad')
        m2.set_price(14)
        m2.set_category('Entrees')
        m2.set_description('caesar salad')
        result = m2.add()
        self.assertTrue(result)

    def test_load_all_menu_items(self):
        m1 = MenuItems.load()
        # print(m1)
        self.assertTrue(len(m1) >= 0)

    def test_select_menu_item(self):
        m1 = MenuItems.build('Fries', 'Entrees', 10, 'potato fries')
        result = m1.add()
        self.assertTrue(result)
        item_id = m1.get_id()
        self.assertTrue(item_id == m1.get_id())
        result = m1.select(item_id)
        self.assertTrue(result)
        self.assertEqual(m1.get_id(), item_id)
        self.assertEqual(m1.get_name(), 'Fries')
        self.assertEqual(m1.get_category(), 'Entrees')
        self.assertEqual(m1.get_price(), 10)
        self.assertEqual(m1.get_description(), 'potato fries')

    def test_update_menu_item(self):
        data = MenuItems.load()
        sample_id = data[7]['id']
        m1 = MenuItems()
        m1.select(sample_id)
        m1.set_price(67)
        m1.set_name('Diet Coke')
        self.assertTrue(m1.update())
