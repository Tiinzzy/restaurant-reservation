from database import Database

import business.seating_tables_class_sql as seatings_tables


class SeatingTables:

    def __init__(self):
        self.__id = None
        self.__seat_count = None
        self.__available = None

    @staticmethod
    def build(seat_count, available):
        seating = SeatingTables()
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
        return self.__available

    def add(self):
        data = (self.__seat_count, self.__available)
        db = Database()
        con, cur = db.open_database()
        cur.execute(seatings_tables.add_sql, data)
        con.commit()
        result = (cur.rowcount == 1)
        self.__id = cur.lastrowid if cur.rowcount == 1 else -1
        db.close_database()
        return result

    @staticmethod
    def select_available_seats(seat_count):
        db = Database()
        con, cur = db.open_database()
        cur.execute(seatings_tables.select_available_sql, (seat_count,))
        rows = cur.fetchall()
        db.close_database()
        data = []
        for row in rows:
            data.append((row[0]))
        return data
    def to_string(self):
        return str(self.__id) + ', ' + str(self.__seat_count) + ', ' + str(self.__available)
