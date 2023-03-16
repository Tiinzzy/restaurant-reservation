from database import Database

import reservation_class_sql as reservation_table


class RootObject:
    def describe(self):
        attrs = [a for a in dir(self) if not a.startswith('__')]
        for a in attrs:
            if a != 'describe':
                print(a+':', getattr(self, a))


class Reservation:
    def __init__(self):
        pass

    @classmethod
    def add(self, user_info):
        data = (user_info['timestamp'],
                user_info['customer_name'],
                int(user_info['customer_id']),
                int(user_info['seat_count']),
                int(user_info['table_id']),
                user_info['for_date'],
                user_info['for_how_long'],
                user_info['status'],
                user_info['latest_comment'],
                int(user_info['waiter_id']),
                user_info['reservation_type'],
                int(user_info['total_price']),
                int(user_info['tip_percent']))
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.add_sql, data)
        rows = cur.fetchall()
        con.commit()
        result = {'count': cur.rowcount}
        db.close_database()
        return result

    @classmethod
    def delete(self, status):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.delete_sql, (status,))
        con.commit()
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def __get_row_with_column(self, row, cursor_description):
        columns = list(map(lambda c: c[0], cursor_description))
        result = RootObject()
        for i in range(len(columns)):
            setattr(result, columns[i], row[i])
            # result[columns[i]] = row[i]
        return result

    @classmethod
    def load(self, id):
        self.id = id
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.load_sql, (int(id),))
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result = self.__get_row_with_column(rows[0], cur.description)
        db.close_database()
        return result

    @classmethod
    def update(self, info):
        data = (info['status'], info['id'])
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.update_sql, data)
        con.commit()
        result = {'count': cur.rowcount}
        db.close_database()
        return result

    @classmethod
    def get_ordero_items(self, id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.order_item_sql, (id,))
        con.commit()
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def add_order_item(self, menu_item_id, count):
        # Method 1 >> insert into order_items (reservation_id, menu_item_id, count) values (self.id, menu_item_id, count)
        # Method 2 >> order = OrderItems()
        #             order.add_item(reservation_id, menu_item_id, count)
        pass

    @classmethod
    def delete_order_item(self, menu_item_id):
        pass

    @classmethod
    def update_order_items(self, menu_item_id, count):
        pass
