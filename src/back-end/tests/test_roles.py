import unittest

from mysql_tables import MysqlTables


class TestRoles(unittest.TestCase):

    def test_drop_create_table(self):
        MysqlTables.create_roles()
        row_count1 = MysqlTables.select_roles_count()

        MysqlTables.create_user_roles()
        row_count2 = MysqlTables.select_user_roles_count()
        
        MysqlTables.create_user()
        row_count3 = MysqlTables.select_user_count()

        MysqlTables.create_menu_items()
        row_count4 = MysqlTables.select_menu_items_count()

        MysqlTables.create_order_items()
        row_count5 = MysqlTables.select_order_items_count()

        MysqlTables.create_seating_tables()
        row_count6 = MysqlTables.select_seating_tables_count()

        MysqlTables.create_reservation()
        row_count7 = MysqlTables.select_reservation_count()
  
        self.assertEqual(row_count7, 0, "test_drop_create_table Failed!")
