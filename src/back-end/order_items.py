from database import Database

import order_items_class_sql as order_items_table

class OrderItems:
    def __init__(self):
        pass

    @classmethod
    def add(self, info):
        data = (int(info['reservation_id']), int(info['menu_item_id']),
                int(info['count']), int(info['total_price']), info['comment'])
        db = Database()
        con, cur = db.open_database()
        cur.execute(order_items_table.add_sql, data)
        con.commit()
        result = {'count': cur.rowcount}
        db.close_database()
        return result

    @classmethod
    def delete(self, name):
        db = Database()
        con, cur = db.open_database()
        sql = """DELETE FROM tests.rr_order_items WHERE name = '%s'"""
        cur.execute(sql, name)
        con.commit()
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
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
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def update(self):
        pass
