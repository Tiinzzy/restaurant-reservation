from database import Database

import menu_items_class_sql as menu_items_table


class RootObject:
    def describe(self):
        attrs = [a for a in dir(self) if not a.startswith('__')]
        # for a in attrs:
        #     if a != 'describe':
        #         print(a+':', getattr(self, a))


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
        result = RootObject()
        setattr(result, 'count', cur.rowcount)
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
            result = self.__get_row_with_column(rows[0], cur.description)
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
    def update(self):
        pass
