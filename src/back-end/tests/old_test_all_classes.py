import unittest

from old_implementation.reservation import Reservation


# from seating_tables import SeatingTables
# from menu_items import MenuItems


class TestAllClasses(unittest.TestCase):
    '''
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
    '''

    def test_reservation_class_methods(self):
        data = {'timestamp': 'timestamp', 'customer_name': 'customer_name', 'customer_id': 134, 'seat_count': 4,
                'table_id': 10,
                'for_date': 'for_date', 'for_how_long': 'for_how_long', 'status': 'status',
                'latest_comment': 'latest_comment', 'waiter_id': 5,
                'reservation_type': 'reservation_type', 'total_price': 65, 'tip_percent': 15}
        r1 = Reservation()
        r1id = r1.add(data)
        self.assertNotEqual(r1id, -1, 'Couldn\'t add data to table')

        r2 = Reservation()
        result2 = r2.load(r1id)
        self.assertEqual(result2.id, r1id)
        self.assertEqual(result2.customer_name, 'customer_name')
        self.assertEqual(result2.waiter_id, 5)
        self.assertEqual(result2.tip_percent, 15)

        data['customer_name'] = 'Ronald Bald'
        data['tip_percent'] = 13
        r2.update_status(data)
        r3 = Reservation()
        result3 = r3.load(r2.get_reservation_id())
        self.assertEqual(result3.customer_name, data['customer_name'])
        self.assertEqual(result3.tip_percent, data['tip_percent'])

        result = r3.delete()
        self.assertEqual(result, 1)
        r4 = Reservation()
        result4 = r4.load(r1id)
        self.assertTrue(result4 is None)

        # result = Reservation.add_order_item(1, 3)
        # self.assertEqual(result.count, 1, 'Couldn\'t add data to table')
        #
        # result = Reservation.update_order_items(1, 5)
        # self.assertEqual(result.count, 1, "Couldn't UPDATE table")
        # result = Reservation().load_order_items()
        # self.assertEqual(result.id, 1, "WRONG ID")
        # self.assertEqual(result.reservation_id, 1, "WRONG RESERVATION ID")
        # self.assertEqual(result.menu_item_id, 1, "WRONG MENU ITEM ID")
        # self.assertEqual(result.count, 5, "WRONG COUNT")
        #
        # result = Reservation.delete_order_item(1)
        # self.assertEqual(len(result), 0)

    '''
    def test_seating_tables_class_methods(self):
        SeatingTables.add(2, 'True')
        SeatingTables.add(4, 'True')
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

        MenuItems.add(data1)
        result = MenuItems.add(data)
        self.assertEqual(result.count, 1, 'Couldn\'t add data to table')

        result = MenuItems.select(1)
        self.assertEqual(result.id, 1, 'Wrong ID')
        self.assertEqual(result.name, 'name', 'Wrong NAME')
        self.assertEqual(result.category, 'category', 'Wrong CATEGORY')
        self.assertEqual(result.price, 28, 'Wrong PRICE')
        self.assertEqual(result.description, 'description',
                         'Wrong DESCRIPTION')

        result = MenuItems.delete(1)
        self.assertEqual(len(result), 0, 'Couldn\'t delete row')
    '''
