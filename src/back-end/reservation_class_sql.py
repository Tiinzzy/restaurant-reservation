add_sql = """
INSERT INTO tests.rr_reservation (timestamp, customer_name, customer_id, seat_count, table_id, for_date, for_how_long, status, latest_comment, waiter_id, reservation_type, total_price, tip_percent)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
"""

load_sql = """
SELECT * FROM tests.rr_reservation
    WHERE id = %s ;
"""

delete_sql = """
DELETE FROM tests.rr_reservation WHERE status = %s ;
"""

update_sql = """UPDATE tests.rr_reservation
    SET status = %s
    WHERE id = %s ; 
"""

order_item_sql = """S
ELECT mi.id as id, mi.count as count, mi.total_price as total FROM tests.rr_reservation res
    join tests.rr_menu_items mi on mi.reservation_id = res.id
    WHERE res.id = %s ;
"""

add_order_items_sql = """
INSERT INTO tests.rr_order_items (reservation_id, menu_item_id, count)
    VALUES(%s,%s,%s);
"""