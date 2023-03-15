from database import Database

import menu_items_class_sql as menu_items_table


class MenuItems:
    def __init__(self):
        pass

    @classmethod
    def add(self, info):
        data = (info['name'],
                info['category'],
                info['price'],
                info['description'])
        db = Database()
        con, cur = db.open_database()
        cur.execute(menu_items_table.add_sql, data)
        con.commit()
        result = {'count': cur.rowcount}
        db.close_database()
        return result

    @classmethod
    def delete(self, id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(menu_items_table.delete_sql, (int(id),))
        con.commit()
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def select(self, id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(menu_items_table.select_sql, (int(id),))
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def update(self):
        pass
