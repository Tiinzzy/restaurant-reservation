import unittest

from mysql_tables import MysqlTables
from users import Users
from reservation import Reservation
from seating_tables import SeatingTables
from menu_items import MenuItems
from order_items import OrderItems


class TestAllClasses(unittest.TestCase):

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
        self.assertEqual(result.count, 1)

        result = Users.insert_into_roles('Customer')
        self.assertEqual(result.count, 1)

        result = Users.insert_into_roles('Waiter')
        self.assertEqual(result.count, 1)

        result = Users.insert_into_roles('Cashier')
        self.assertEqual(result.count, 1)

        result = Users.select_all_roles()
        roles = set(list(map(lambda x: x[1], result)))

        self.assertTrue('Admin' in roles)
        self.assertTrue('Customer' in roles)
        self.assertTrue('Waiter' in roles)
        self.assertTrue('Cashier' in roles)

    def test_user_class_methods(self):
        data = {'name': 'name', 'lastName': 'lastName', 'email': 'email',
                'password': 'password', 'birthday': 'birthday'}
        result = Users.add(data)
        self.assertEqual(result['count'], 1)

        result = Users.load('email')
        result.describe()
        self.assertEqual(result.name, 'name')
        self.assertEqual(result.lastName, 'lastName')
        self.assertEqual(result.email, 'email')
        self.assertEqual(result.password, 'password')
        self.assertEqual(result.birthday, 'birthday')

        result = Users.delete('email')
        self.assertEqual(len(result), 0, 'Didnd\'t delete the row')

    def test_reservation_class_methods(self):
        data = {'timestamp': 'timestamp', 'customer_name': 'customer_name', 'customer_id': 134, 'seat_count': 4, 'table_id': 10,
                'for_date': 'for_date', 'for_how_long': 'for_how_long', 'status': 'status', 'latest_comment': 'latest_comment', 'waiter_id': 5,
                'reservation_type': 'reservation_type', 'total_price': 65, 'tip_percent': 15}
        result = Reservation.add(data)
        self.assertEqual(result.count, 1, 'Couldn\'t add data to table')

        result = Reservation.load(1)
        self.assertEqual(result.id, 1, 'Wrong ID')
        self.assertEqual(result.timestamp, 'timestamp', 'Wrong TIMESTAMP')
        self.assertEqual(result.customer_name,
                         'customer_name', 'Wrong CUSTOMER NAME')
        self.assertEqual(result.customer_id, 134, 'Wrong CUSTOMER ID')
        self.assertEqual(result.seat_count, 4, 'Wrong SEAT COUNT')
        self.assertEqual(result.table_id, 10, 'Wrong TABLE ID')
        self.assertEqual(result.for_date, 'for_date', 'Wrong FOR DATE')
        self.assertEqual(result.for_how_long,
                         'for_how_long', 'Wrong FOR HOW LONG')
        self.assertEqual(result.status, 'status', 'Wrong STATUS')
        self.assertEqual(result.latest_comment,
                         'latest_comment', 'Wrong LATEST COMMENT')
        self.assertEqual(result.waiter_id, 5, 'Wrong WAITER ID')
        self.assertEqual(result.reservation_type,
                         'reservation_type', 'Wrong RESERVATION TYPE')
        self.assertEqual(result.total_price, 65, 'Wrong TOTAL PRICE')
        self.assertEqual(result.tip_percent, 15, 'Wrong TIP PERCENT')

        data = {'status': 'Arrived', 'id': 1}
        result = Reservation.update(data)
        self.assertEqual(result.count, 1, "Couldn't UPDATE table")
        result = Reservation.load(1)
        self.assertEqual(result.status, 'Arrived', 'Wrong STATUS')

        result = Reservation.add_order_item(1,3)
        self.assertEqual(result.count, 1, 'Couldn\'t add data to table')

        result = Reservation.delete_order_item(1)
        self.assertEqual(len(result), 0)

        result = Reservation.delete('status')
        self.assertEqual(len(result), 0)

    def test_seating_tables_class_methods(self):
        result = SeatingTables.add(2, 'True')
        result = SeatingTables.add(4, 'True')
        result = SeatingTables.add(2, 'False')
        self.assertEqual(result.count, 1,
                         'Couldn\'t add DATA to SEATING TABLES!')

        result = SeatingTables.select(2)
        self.assertEqual(result.id, 1, 'NO TABLE AVAILABLE!')

        result = SeatingTables.update('False', 1)
        self.assertEqual(result.count, 1, "Couldn't UPDATE table")
        result = SeatingTables.load(1)
        self.assertEqual(result.available, 'False',
                         'Wrong UPDATE HAPPENED!')

        result = SeatingTables.delete(1)
        self.assertEqual(len(result), 0, 'Couldn\'t delete row')

    def test_menu_items_class_methods(self):
        data = {'name': 'name', 'category': 'category',
                'price': 16, 'description': 'description'}

        data1 = {'name': 'name', 'category': 'category',
                 'price': 28, 'description': 'description'}

        result = MenuItems.add(data1)
        result = MenuItems.add(data)
        self.assertEqual(result['count'], 1, 'Couldn\'t add data to table')

        result = MenuItems.select(1)
        self.assertEqual(result['data_row'][0], 1, 'Wrong ID')
        self.assertEqual(result['data_row'][1], 'name', 'Wrong NAME')
        self.assertEqual(result['data_row'][2], 'category', 'Wrong CATEGORY')
        self.assertEqual(result['data_row'][3], 28, 'Wrong PRICE')
        self.assertEqual(result['data_row'][4],
                         'description', 'Wrong DESCRIPTION')

        result = MenuItems.delete(1)
        self.assertEqual(len(result), 0, 'Couldn\'t delete row')

    # def test_order_items_class_methods(self):
    #     data = {'reservation_id': 1, 'menu_item_id': 1,
    #             'count': 3, 'total_price': 43, 'comment': 'comment'}
    #     result = OrderItems.add(data)
    #     self.assertEqual(result['count'], 1, 'Couldn\'t add data to table')

    #     result = OrderItems.delete(1)
    #     self.assertEqual(len(result), 0, 'Couldn\'t delete row')
