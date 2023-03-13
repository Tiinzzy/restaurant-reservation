from database import Database


class MenuItems:
    def __init__(self):
        pass

    @classmethod
    def add(self, name, category, price, description):
        db = Database()
        con, cur = db.open_database()
        sql = """INSERT INTO tests.rr_menu_items (name, category, price, description)
                VALUES(%s,%s,%s,%s,%s)"""
        data = (name, category, price, description)
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
        sql = """DELETE FROM tests.rr_menu_items WHERE name = '%s'"""
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
        sql = """SELECT * FROM tests.rr_menu_items WHERE"""
        cur.execute(sql)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({'all_menu_items': row[0]})
        db.close_database()
        return result

    @classmethod
    def update(self):
        pass