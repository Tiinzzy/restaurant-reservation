import unittest

from mysql_tables import MysqlTables


class TestRoles(unittest.TestCase):

    def test_drop_create_table(self):
        MysqlTables.create_roles()
        row_count1 = MysqlTables.select_roles_count()

        MysqlTables.create_user_roles()
        row_count2 = MysqlTables.select_user_roles_count()
        
        if row_count1 == 0 and row_count2 == 0:
            row_count = 0
        else:
            row_count = -1    
        self.assertEqual(row_count, 0, "test_drop_create_table Failed!")
