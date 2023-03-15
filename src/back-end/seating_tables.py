from database import Database

import seatin_class_sql as seating_tables


class SeatingTables:
    def __init__(self):
        pass

    @classmethod
    def add(self, seat_count, available):
        db = Database()
        con, cur = db.open_database()
        data = (int(seat_count), available)
        cur.execute(seating_tables.add_sql, data)
        rows = cur.fetchall()
        con.commit()
        result = {'count': cur.rowcount}
        db.close_database()
        return result

    @classmethod
    def delete(self, id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_tables.delete_sql, (int(id),))
        rows = cur.fetchall()
        con.commit()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def select(self, seat_count):
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_tables.select_sql, (int(seat_count),))
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def update(self, available, id):
        db = Database()
        con, cur = db.open_database()
        sql = """UPDATE tests.rr_seating_tables
                SET available = '%s'
                WHERE id = '%s'"""
        data = (available, id)
        cur.execute(sql, data)
        con.commit()
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(
                {'result': row[0]})
        db.close_database()
        return result
