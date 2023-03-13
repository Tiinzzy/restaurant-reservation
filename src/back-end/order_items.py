from database import Database


class OrderItems:
    def __init__(self):
        pass

    @classmethod
    def add(self, reservation_id, menu_item_id, count, total_price, comment):
        db = Database()
        con, cur = db.open_database()
        sql = """INSERT INTO tests.rr_order_items (reservation_id, menu_item_id, count, total_price, comment)
                VALUES(%s,%s,%s,%s,%s)"""
        data = (reservation_id, menu_item_id, count, total_price, comment)
        cur.execute(sql, data)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({'result': row[0]})
        db.close_database()

        return result

    @classmethod
    def delete(self, name):
        db = Database()
        con, cur = db.open_database()
        sql = """DELETE FROM tests.rr_order_items WHERE name = '%s'"""
        cur.execute(sql, name)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({'result': row[0]})
        db.close_database()
        return result

    @classmethod
    def select(self):
        db = Database()
        con, cur = db.open_database()
        sql = """SELECT mi.name as name, mi.category as category, mi.price as price FROM tests.rr_order_items oi
        join tests.rr_menu_items mi on mi.id = oi.menu_item_id"""
        cur.execute(sql)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({'name': row[0], 'category': row[1], 'price': row[2]})
        db.close_database()
        return result

    @classmethod
    def update(self):
        pass
