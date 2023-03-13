from database import Database


class SeatingTables:
    def __init__(self):
        pass

    @classmethod
    def add(self, seat_count, available):
        db = Database()
        con, cur = db.open_database()
        sql = """INSERT INTO tests.rr_tables (seat_count, available)
                VALUES(%s,%s)"""
        data = (seat_count, available)
        cur.execute(sql, data)
        rows = cur.fetchall()
        con.commit()
        result = []
        for row in rows:
            result.append({'result': row[0]})
        db.close_database()

        return result

    @classmethod
    def delete(self, id):
        db = Database()
        con, cur = db.open_database()
        sql = """DELETE FROM tests.rr_tables WHERE id = '%s'"""
        cur.execute(sql, id)
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
        sql = """SELECT id, seat_count FROM tests.rr_tables
                WHER available = 'true'"""
        cur.execute(sql)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(
                {'available_tables': row[0], 'seat_count': row[1]})
        db.close_database()
        return result

    @classmethod
    def update(self, available, id):
        db = Database()
        con, cur = db.open_database()
        sql = """UPDATE tests.rr_tables
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
