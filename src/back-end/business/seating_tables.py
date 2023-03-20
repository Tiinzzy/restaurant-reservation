from database import Database
import business.users_class_sql as users_table


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

    def to_string(self):
        return str(self.__id) + ', ' + str(self.__seat_count) + ', ' + str(self.__available)
