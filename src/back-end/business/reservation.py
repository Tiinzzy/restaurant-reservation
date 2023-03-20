class Reservation:

    def __int__(self):
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

    @staticmethod
    def build(timestamp, customer_name, customer_id, seat_count, table_id, for_date, for_how_long, status,
              latest_comment, waiter_id, reservation_type, total_price, tip_percent):
        reservation = Reservation()
        reservation.__timestamp = timestamp
        reservation.__customer_name = customer_name
        reservation.__customer_id = customer_id
        reservation.__seat_count = seat_count
        reservation.__table_id = table_id
        reservation.__for_date = for_date
        reservation.__for_how_long = for_how_long
        reservation.__status = status
        reservation.__latest_comment = latest_comment
        reservation.__waiter_id = waiter_id
        reservation.__reservation_type = reservation_type
        reservation.__total_price = total_price
        reservation.__tip_percent = tip_percent
        return reservation

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

    def to_string(self):
        return str(self.__id) + ', ' + str(self.__timestamp) + ', ' + str(self.__customer_name) + ', ' + \
            str(self.__customer_id) + ', ' + str(self.__seat_count) + ', ' + str(self.__table_id) + ', ' + \
            str(self.__for_date) + ', ' + str(self.__for_how_long) + ', ' + str(self.__status) + ', ' + \
            str(self.__latest_comment) + ', ' + str(self.__waiter_id) + ', ' + \
            str(self.__reservation_type) + ', ' + str(self.__total_price) + ', ' + str(self.__tip_percent)
