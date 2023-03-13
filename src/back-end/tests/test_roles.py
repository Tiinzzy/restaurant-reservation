import unittest

from mysql_tables import Tables


class TestRoles(unittest.TestCase):
    
    def test_drop_create_table(self):
        Tables.create_roles()
        row_count = Tables.select_roles_count()
        self.assertEqual(row_count, 0, "test_drop_create_table Failed!")
