from database import Database
import reservation_class_sql as reservation_table


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
        con.commit()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def load(self, id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.load_sql, (int(id),))
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
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
        result = []
        for row in rows:
            result.append(
                {'menu_item_id': row[0], 'count': row[1], 'total': row[2]})
        db.close_database()
        return result

    @classmethod
    def add_ordero_items(self):
        pass

    @classmethod
    def delete_ordero_items(self):
        pass

    @classmethod
    def update_ordero_items(self):
        pass
