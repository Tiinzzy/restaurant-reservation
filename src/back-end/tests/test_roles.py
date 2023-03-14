import unittest

from mysql_tables import MysqlTables


class TestRoles(unittest.TestCase):
    
    def test_drop_create_table(self):
        MysqlTables.create_roles()
        row_count = MysqlTables.select_roles_count()

        # MysqlTables.create_user_roles()
        # row_count = MysqlTables.select_user_roles_count()
        self.assertEqual(row_count, 0, "test_drop_create_table Failed!")


