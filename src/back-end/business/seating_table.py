from database import Database

import business.seating_table_class_sql as seating_table


class SeatingTable:

    def __init__(self):
        self.__id = None
        self.__seat_count = None
        self.__available = None

    @staticmethod
    def build(seat_count, available):
        seating = SeatingTable()
        seating.__seat_count = seat_count
        seating.__available = available
        return seating

    def get_id(self):
        return self.__id

    def set_seat_count(self, count):
        self.__seat_count = count

    def get_seat_count(self):
        return self.__seat_count

    def set_available(self, result):
        self.__available = result

    def get_available(self):
        if self.__available is None:
            return None
        else:
            return self.__available == 1

    def add(self):
        data = (self.__seat_count, self.__available)
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_table.add_sql, data)
        con.commit()
        result = (cur.rowcount == 1)
        self.__id = cur.lastrowid if cur.rowcount == 1 else -1
        db.close_database()
        return result

    @staticmethod
    def select_available_seats(seat_count):
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_table.select_available_sql, (seat_count,))
        rows = cur.fetchall()
        db.close_database()
        data = []
        for row in rows:
            data.append({'seat_id': row[0]})
        return data

    def load(self, table_id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_table.load_sql, (table_id,))
        rows = cur.fetchall()
        db.close_database()
        if len(rows) == 1:
            self.__id = rows[0][0]
            self.__seat_count = rows[0][1]
            self.__available = rows[0][2]
            return True
        else:
            return False

    def update(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_table.update_sql, (self.__available, self.__seat_count, self.__id))
        con.commit()
        result = (cur.rowcount == 1)
        db.close_database()
        return result

    def delete(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_table.delete_sql, (self.__id,))
        con.commit()
        result = (cur.rowcount == 1)
        db.close_database()
        return result

    @staticmethod
    def select_all_seating_tables():
        db = Database()
        con, cur = db.open_database()
        cur.execute(seating_table.select_all_sql)
        rows = cur.fetchall()
        db.close_database()
        data = []
        for row in rows:
            data.append({'id': row[0], 'seat_count': row[1], 'available': row[2]})
        return data

    def to_string(self):
        return str(self.__id) + ', ' + str(self.__seat_count) + ', ' + str(self.__available)
