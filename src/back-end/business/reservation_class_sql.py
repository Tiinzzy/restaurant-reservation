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

update_sql = """
UPDATE tests.rr_reservation SET timestamp = %s , customer_name = %s , customer_id = %s , seat_count = %s , table_id = %s 
    , for_date = %s , for_how_long = %s , status = %s , latest_comment = %s , waiter_id = %s , reservation_type = %s 
    , total_price = %s , tip_percent = %s
    WHERE id = %s ; 
"""
