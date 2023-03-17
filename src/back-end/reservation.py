from database import Database

import reservation_class_sql as reservation_table


class RootObject:
    @classmethod
    def describe(cls):
        attrs = [a for a in dir(cls) if not a.startswith('__')]
        for a in attrs:
            if a != 'describe':
                print(a + ':', getattr(cls, a))


class Reservation:
    reservation_id = -1

    def __init__(self):
        pass

    def get_reservation_id(self):
        return self.reservation_id

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
        con.commit()
        self.reservation_id = cur.lastrowid if cur.rowcount == 1 else -1
        db.close_database()
        return self.reservation_id

    def load(self, reservation_id):
        self.reservation_id = reservation_id
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.load_sql, (self.reservation_id,))
        rows = cur.fetchall()
        result = None
        if len(rows) == 1:
            result = self.__get_row_with_column(rows[0], cur.description)
        db.close_database()
        return result

    def update_status(self, user_info):
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
                int(user_info['tip_percent']),
                self.reservation_id)
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.update_sql, data)
        con.commit()
        result = cur.rowcount
        db.close_database()
        return result

    def delete(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.delete_sql, (self.reservation_id,))
        con.commit()
        result = cur.rowcount
        db.close_database()
        return result

    @classmethod
    def __get_row_with_column(cls, row, cursor_description):
        columns = list(map(lambda c: c[0], cursor_description))
        result = RootObject()
        for i in range(len(columns)):
            setattr(result, columns[i], row[i])
            # result[columns[i]] = row[i]
        return result

    @classmethod
    def get_order_items(cls, reservation_id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.order_item_sql, (reservation_id,))
        con.commit()
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def add_order_item(cls, menu_item_id, count):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.add_order_items_sql,
                    (cls.reservation_id, menu_item_id, count))
        con.commit()
        result = RootObject()
        setattr(result, 'count', cur.rowcount)
        db.close_database()
        return result

    @classmethod
    def delete_order_item(cls, menu_item_id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.delete_order_items_sql, (menu_item_id,))
        con.commit()
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def update_order_items(cls, menu_item_id, count):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.update_order_items_sql,
                    (count, menu_item_id))
        con.commit()
        result = RootObject()
        setattr(result, 'count', cur.rowcount)
        db.close_database()
        return result

    def load_order_items(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.load_order_items_sql, (self.reservation_id,))
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result = self.__get_row_with_column(rows[0], cur.description)
        db.close_database()
        return result
