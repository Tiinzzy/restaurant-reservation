import unittest

from mysql_tables import MysqlTables

from users import Users


class TestRoles(unittest.TestCase):

    # def test_drop_create_roles(self):
    #     MysqlTables.create_roles()
    #     row_count = MysqlTables.select_roles_count()
    #     self.assertEqual(row_count, 0, "Create Table ROLES Failed!")

    def test_drop_create_user_roles(self):
        MysqlTables.create_user_roles()
        row_count = MysqlTables.select_user_roles_count()
        self.assertEqual(row_count, 0, "Create Table USER-ROLES Failed!")

    def test_drop_create_user(self):
        MysqlTables.create_user()
        row_count = MysqlTables.select_user_count()
        self.assertEqual(row_count, 0, "Create Table USER Failed!")

    def test_drop_create_menu_items(self):
        MysqlTables.create_menu_items()
        row_count = MysqlTables.select_menu_items_count()
        self.assertEqual(row_count, 0, "Create Table MENU-ITEMS Failed!")

    def test_drop_create_order_items(self):
        MysqlTables.create_order_items()
        row_count = MysqlTables.select_order_items_count()
        self.assertEqual(row_count, 0, "Create Table MENU-ITEMS Failed!")

    def test_drop_create_seating_tables(self):
        MysqlTables.create_seating_tables()
        row_count = MysqlTables.select_seating_tables_count()
        self.assertEqual(row_count, 0, "Create Table SEATING-TABLES Failed!")

    def test_drop_create_reservation(self):
        MysqlTables.create_reservation()
        row_count = MysqlTables.select_reservation_count()
        self.assertEqual(row_count, 0, "Create Table RESERVATION Failed!")

    def test_select_roles(self):
        result = Users.select_all_roles()

        self.assertEqual(result[0][1], 'Admin')
        self.assertEqual(result[1][1], 'Customer')
        self.assertEqual(result[2][1], 'Waiter')
        self.assertEqual(result[3][1], 'Cashier')

    # def test_user_class_methods(self):
    #     result = Users.add('name', 'lastName', 'email', 'password', 'birthday')
    #     self.assertEqual(result['count'], 1)

    #     result = Users.load('email')
    #     self.assertEqual(result['data_row'][1], 'name')
    #     self.assertEqual(result['data_row'][2], 'lastName')
    #     self.assertEqual(result['data_row'][3], 'email')
    #     self.assertEqual(result['data_row'][4], 'password')
    #     self.assertEqual(result['data_row'][5], 'birthday')
