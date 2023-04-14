from database import Database
import business.reservation_class_sql as reservation_table

STATUS_TYPE = ['Just walked in', 'Here sitting', 'Left', 'Completed', 'Reserved', 'Cancelled']
RESERVATION_TYPE = ['Phone', 'Online', 'In person']


class Reservation:

    def __init__(self):
        self.__id = None
        self.__timestamp = None
        self.__customer_name = None
        self.__customer_id = None
        self.__seat_count = None
        self.__table_id = None
        self.__for_date = None
        self.__for_how_long = None
        self.__status = None
        self.__latest_comment = None
        self.__waiter_id = None
        self.__reservation_type = None
        self.__total_price = None
        self.__tip_percent = None

    def set_timestamp(self, timestamp):
        self.__timestamp = timestamp

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_seat_count(self, seat_count):
        self.__seat_count = seat_count

    def set_table_id(self, table_id):
        self.__table_id = table_id

    def set_for_date(self, for_date):
        self.__for_date = for_date

    def set_for_how_long(self, for_how_long):
        self.__for_how_long = for_how_long

    def set_status(self, status):
        self.__status = status

    def set_latest_comment(self, latest_comment):
        self.__latest_comment = latest_comment

    def set_waiter_id(self, waiter_id):
        self.__waiter_id = waiter_id

    def set_reservation_type(self, reservation_type):
        self.__reservation_type = reservation_type

    def set_total_price(self, total_price):
        self.__total_price = total_price

    def set_tip_percent(self, tip_percent):
        self.__tip_percent = tip_percent

    def get_id(self):
        return self.__id

    def get_timestamp(self):
        return self.__timestamp

    def get_customer_name(self):
        return self.__customer_name

    def get_customer_id(self):
        return self.__customer_id

    def get_seat_count(self):
        return self.__seat_count

    def get_table_id(self):
        return self.__table_id

    def get_for_date(self):
        return self.__for_date

    def get_for_how_long(self):
        return self.__for_how_long

    def get_status(self):
        return self.__status

    def get_latest_comment(self):
        return self.__latest_comment

    def get_waiter_id(self):
        return self.__waiter_id

    def get_reservation_type(self):
        return self.__reservation_type

    def get_total_price(self):
        return self.__total_price

    def get_tip_percent(self):
        return self.__tip_percent

    def __is_ok_to_save(self):
        if self.__status is None or self.__status not in STATUS_TYPE:
            return False

        if self.__reservation_type is None or self.__reservation_type not in RESERVATION_TYPE:
            return False

        return True

    def add(self):
        if not self.__is_ok_to_save():
            return False

        data = (
            self.__timestamp, self.__customer_name, self.__customer_id, self.__seat_count, self.__table_id,
            self.__for_date,
            self.__for_how_long, self.__status, self.__latest_comment, self.__waiter_id, self.__reservation_type,
            self.__total_price, self.__tip_percent)
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.add_sql, data)
        con.commit()
        result = (cur.rowcount == 1)
        self.__id = cur.lastrowid if cur.rowcount == 1 else -1
        db.close_database()
        return result

    def load(self, reservation_id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.load_sql, (reservation_id,))
        rows = cur.fetchall()
        db.close_database()

        if len(rows) == 1:
            self.__id = rows[0][0]
            self.__timestamp = rows[0][1]
            self.__customer_name = rows[0][2]
            self.__customer_id = rows[0][3]
            self.__seat_count = rows[0][4]
            self.__table_id = rows[0][5]
            self.__for_date = rows[0][6]
            self.__for_how_long = rows[0][7]
            self.__status = rows[0][8]
            self.__latest_comment = rows[0][9]
            self.__waiter_id = rows[0][10]
            self.__reservation_type = rows[0][11]
            self.__total_price = rows[0][12]
            self.__tip_percent = rows[0][13]
            return True
        else:
            return False

    @staticmethod
    def select_all():
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.select_all_sql)
        rows = cur.fetchall()
        db.close_database()
        data = []
        for row in rows:
            data.append({'id': row[0], 'timestamp': row[1], 'customer_name': row[2], 'customer_id': row[3],
                         'seat_count': row[4], 'table_id': row[5], 'for_date': row[6],
                         'for_how_long': row[7], 'status': row[8], 'comment': row[9], 'waiter_id': row[10],
                         'reservation_type': row[11], 'total_price': row[12], 'tip_percent': row[13]})
        return data

    def update(self):
        if not self.__is_ok_to_save:
            return False

        data = (
            self.__timestamp, self.__customer_name, self.__customer_id, self.__seat_count, self.__table_id,
            self.__for_date,
            self.__for_how_long, self.__status, self.__latest_comment, self.__waiter_id, self.__reservation_type,
            self.__total_price, self.__tip_percent, self.__id)
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.update_sql, data)
        con.commit()
        result = (cur.rowcount == 1)
        db.close_database()
        return result

    def select_all_order_items(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.select_all_order_items_sql, (self.__id,))
        rows = cur.fetchall()
        db.close_database()
        data = []
        for row in rows:
            data.append({"order_item_id": row[0], "reservation_id": row[1], "menu_item_id": row[2], "count": row[3], 'name': row[4]})
        return data

    def add_order_item(self, menu_item_id, count):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.add_order_item_sql, (self.__id, menu_item_id, count))
        con.commit()
        result = (cur.rowcount == 1)
        db.close_database()
        return result

    def delete_order_item(self, menu_item_id, order_item_id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.delete_order_item_sql, (self.__id, menu_item_id, order_item_id))
        con.commit()
        result = (cur.rowcount == 1)
        db.close_database()
        return result

    def update_order_item(self, order_item_id, count):
        db = Database()
        con, cur = db.open_database()
        cur.execute(reservation_table.update_order_item_sql, (count, self.__id, order_item_id))
        con.commit()
        result = (cur.rowcount == 1)
        db.close_database()
        return result

    def to_string(self):
        return str(self.__id) + ', ' + str(self.__timestamp) + ', ' + str(self.__customer_name) + ', ' + \
            str(self.__customer_id) + ', ' + str(self.__seat_count) + ', ' + str(self.__table_id) + ', ' + \
            str(self.__for_date) + ', ' + str(self.__for_how_long) + ', ' + str(self.__status) + ', ' + \
            str(self.__latest_comment) + ', ' + str(self.__waiter_id) + ', ' + \
            str(self.__reservation_type) + ', ' + str(self.__total_price) + ', ' + str(self.__tip_percent)

    def to_json(self):
        obj = {"id": self.__id, "timestamp": self.__timestamp, "customer_name": self.__customer_name,
               "customer_id": self.__customer_id, "seat_count": self.__seat_count, "table_id": self.__table_id,
               "for_date": self.__for_date, "for_how_long": self.__for_how_long, "status": self.__status,
               "latest_comment": self.__latest_comment, "waiter_id": self.__waiter_id,
               "reservation_type": self.__reservation_type, "total_price": self.__total_price,
               "tip_percent": self.__tip_percent}
        return obj
