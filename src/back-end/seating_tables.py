from database import Database

import seating_class_sql as seating_tables


class RootObject:
    @classmethod
    def describe(cls):
        attrs = [a for a in dir(cls) if not a.startswith('__')]
        for a in attrs:
            if a != 'describe':
                print(a+':', getattr(cls, a))


class SeatingTables:
    def __init__(self):
        pass

    @classmethod
    def add(cls, seat_count, available):
        db = Database()
        con, cur = db.open_database()
        data = (int(seat_count), available)
        cur.execute(seating_tables.add_sql, data)
        con.commit()
        result = RootObject()
        setattr(result, 'count', cur.rowcount)
        db.close_database()
        return result

    @classmethod
    def delete(cls, seating_id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_tables.delete_sql, (int(seating_id),))
        con.commit()
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def select(cls, seat_count):
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_tables.select_sql, (int(seat_count),))
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result = cls.__get_row_with_column(rows[0], cur.description)
        db.close_database()
        return result

    @classmethod
    def update(cls, available, seating_id):
        db = Database()
        con, cur = db.open_database()
        data = (available, int(seating_id))
        cur.execute(seating_tables.update_sql, data)
        con.commit()
        result = RootObject()
        setattr(result, 'count', cur.rowcount)
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
    def load(cls, seating_id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_tables.load_sql, (int(seating_id),))
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result = cls.__get_row_with_column(rows[0], cur.description)
        db.close_database()
        return result
