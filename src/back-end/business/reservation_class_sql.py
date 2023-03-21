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

select_all_order_items_sql = """
SELECT oi.id as id, oi.reservation_id as reservation_id, oi.menu_item_id as menu_item_id, oi.count as count FROM 
    tests.rr_reservation res 
    JOIN tests.rr_order_items oi on oi.reservation_id = res.id
    WHERE res.id = %s ;
"""

add_order_item_sql = """
INSERT INTO tests.rr_order_items (reservation_id, menu_item_id, count)
    VALUES(%s,(SELECT id FROM tests.rr_menu_items mi WHERE mi.name = %s),%s);
"""

delete_order_item_sql = """
DELETE FROM tests.rr_order_items WHERE reservation_id = %s 
    AND menu_item_id = (SELECT id FROM tests.rr_menu_items mi WHERE mi.name = %s);
"""

update_order_item_sql = """
UPDATE tests.rr_order_items SET  menu_item_id = (SELECT id FROM tests.rr_menu_items mi WHERE mi.name = %s), count = %s
    WHERE reservation_id = %s ; 
"""
