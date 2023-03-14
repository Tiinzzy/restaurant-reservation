import unittest

from mysql_tables import MysqlTables


class TestRoles(unittest.TestCase):

    def test_drop_create_table(self):
        MysqlTables.create_roles()
        row_count = MysqlTables.select_roles_count()
        print(row_count)

        MysqlTables.create_user_roles()
        row_count = MysqlTables.select_user_roles_count()
        print(row_count)

        MysqlTables.create_user()
        row_count = MysqlTables.select_user_count()
        print(row_count)

        MysqlTables.create_menu_items()
        row_count = MysqlTables.select_menu_items_count()
        print(row_count)

        MysqlTables.create_order_items()
        row_count = MysqlTables.select_order_items_count()
        print(row_count)

        MysqlTables.create_seating_tables()
        row_count = MysqlTables.select_seating_tables_count()
        print(row_count)

        MysqlTables.create_reservation()
        row_count = MysqlTables.select_reservation_count()
        print(row_count)

        self.assertEqual(row_count, 0, "test_drop_create_table Failed!")
