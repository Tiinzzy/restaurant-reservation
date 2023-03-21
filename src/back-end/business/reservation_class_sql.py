add_sql = """
INSERT INTO tests.rr_reservation (timestamp, customer_name, customer_id, seat_count, table_id, for_date, for_how_long, 
    status, latest_comment, waiter_id, reservation_type, total_price, tip_percent)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
"""