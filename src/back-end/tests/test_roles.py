import unittest

from mysql_tables import MysqlTables
from users import Users
from reservation import Reservation


class TestRoles(unittest.TestCase):

    def test_drop_create_roles(self):
        MysqlTables.create_roles()
        row_count = MysqlTables.select_roles_count()
        self.assertEqual(row_count, 0, "Create Table ROLES Failed!")

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
        result = Users.insert_into_roles('Admin')
        self.assertEqual(result['count'], 1)

        result = Users.insert_into_roles('Customer')
        self.assertEqual(result['count'], 1)

        result = Users.insert_into_roles('Waiter')
        self.assertEqual(result['count'], 1)

        result = Users.insert_into_roles('Cashier')
        self.assertEqual(result['count'], 1)

        result = Users.select_all_roles()
        self.assertEqual(result[0][1], 'Admin')
        self.assertEqual(result[1][1], 'Customer')
        self.assertEqual(result[2][1], 'Waiter')
        self.assertEqual(result[3][1], 'Cashier')

    def test_user_class_methods(self):
        data = {'name': 'name', 'lastName': 'lastName', 'email': 'email',
                'password': 'password', 'birthday': 'birthday'}
        result = Users.add(data)
        self.assertEqual(result['count'], 1)

        result = Users.load('email')
        self.assertEqual(result['data_row'][1], 'name')
        self.assertEqual(result['data_row'][2], 'lastName')
        self.assertEqual(result['data_row'][3], 'email')
        self.assertEqual(result['data_row'][4], 'password')
        self.assertEqual(result['data_row'][5], 'birthday')

        result = Users.delete('email')
        self.assertEqual(len(result), 0, 'Didnd\'t delete the row')

    def test_reservation_class_methods(self):
        data = {'timestamp': 'timestamp', 'customer_name': 'customer_name', 'customer_id': 134, 'seat_count': 4, 'table_id': 10,
                'for_date': 'for_date', 'for_how_long': 'for_how_long', 'status': 'status', 'latest_comment': 'latest_comment', 'waiter_id': 5,
                'reservation_type': 'reservation_type', 'total_price': 65, 'tip_percent': 15}
        result = Reservation.add(data)
        self.assertEqual(result['count'], 1)
