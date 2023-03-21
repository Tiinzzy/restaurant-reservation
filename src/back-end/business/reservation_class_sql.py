add_sql = """
INSERT INTO tests.rr_reservation (timestamp, customer_name, customer_id, seat_count, table_id, for_date, for_how_long, 
    status, latest_comment, waiter_id, reservation_type, total_price, tip_percent)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
"""

load_sql = """
SELECT * FROM tests.rr_reservation WHERE id = %s ; 
"""

select_all_sql = """
SELECT * FROM tests.rr_reservation order by id limit 500; 
"""
