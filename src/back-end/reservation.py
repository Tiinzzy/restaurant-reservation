from database import Database


class Reservation:
    def __init__(self):
        pass

    @classmethod
    def add(self, timestamp, customer_name, customer_id, name, seat_count, table_id, for_date, for_how_long, status, latest_comment, waiter_id, total_price, tip_percent):
        db = Database()
        con, cur = db.open_database()
        sql = """INSERT INTO tests.rr_reservation (timestamp, customer_name, customer_id, name, seat_count, table_id, for_date, for_how_long, status, latest_comment, waiter_id, total_price, tip_percent)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        data = (timestamp, customer_name, customer_id, name, seat_count, table_id, for_date,
                for_how_long, status, latest_comment, waiter_id, total_price, tip_percent)
        cur.execute(sql, data)
        rows = cur.fetchall()
        con.commit()
        result = []
        for row in rows:
            result.append({'result': row[0]})
        db.close_database()

        return result

    @classmethod
    def delete(self, status):
        db = Database()
        con, cur = db.open_database()
        sql = """DELETE FROM tests.rr_reservation WHERE status = '%s'"""
        cur.execute(sql, status)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({'result': row[0]})
        db.close_database()
        return result

    @classmethod
    def load(self, id):
        db = Database()
        con, cur = db.open_database()
        sql = """SELECT * tests.rr_reservation
                WHER id = '%s'"""
        cur.execute(sql, id)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(
                {'id': row[0], 'timestamp': row[1], 'customer_name': row[2], 'customer_id': row[3], 'name': row[4], 'seat_count': row[5], 'table_id': row[6],
                 'for_date': row[7], 'for_how_long': row[8], 'status': row[9], 'latest_comment': row[10], 'waiter_id': row[11], 'total_price': row[12], 'tip_percent': row[13]})
        db.close_database()
        return result

    @classmethod
    def update(self, status, id):
        db = Database()
        con, cur = db.open_database()
        sql = """UPDATE tests.rr_reservation
                SET status = '%s'
                WHERE id = '%s'"""
        data = (status, id)
        cur.execute(sql, data)
        con.commit()
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(
                {'result': row[0]})
        db.close_database()
        return result

    @classmethod
    def get_ordero_items(self, id):
        db = Database()
        con, cur = db.open_database()
        sql = """SELECT mi.id as id, mi.count as count, mi.total_price as total FROM tests.rr_reservation res
        join tests.rr_menu_items mi on mi.reservation_id = res.id
        WHERE res.id = '%s'"""
        cur.execute(sql, id)
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
