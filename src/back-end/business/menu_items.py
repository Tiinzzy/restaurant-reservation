from database import Database

import business.menu_items_class_sql as menu_items_table


class MenuItems:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__category = None
        self.__price = None
        self.__description = None

    @staticmethod
    def build(name, category, price, description):
        item = MenuItems()
        item.__name = name
        item.__category = category
        item.__price = price
        item.__description = description
        return item

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_category(self, category):
        self.__category = category

    def get_category(self):
        return self.__category

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def add(self):
        data = (self.__name, self.__category, self.__price, self.__description)
        db = Database()
        con, cur = db.open_database()
        cur.execute(menu_items_table.add_sql, data)
        con.commit()
        result = (cur.rowcount == 1)
        self.__id = cur.lastrowid if cur.rowcount == 1 else -1
        db.close_database()
        return result

    def delete(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(menu_items_table.delete_sql, (self.__id,))
        con.commit()
        result = (cur.rowcount == 1)
        db.close_database()
        return result

    @staticmethod
    def load():
        db = Database()
        con, cur = db.open_database()
        cur.execute(menu_items_table.load_sql)
        rows = cur.fetchall()
        db.close_database()
        data = []
        for row in rows:
            data.append({'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3], 'description': row[4]})
        return data

    def to_string(self):
        return str(self.__id) + ', ' + str(self.__name) + ', ' + str(self.__category) + ', ' + str(
            self.__price) + ', ' + str(self.__description)
