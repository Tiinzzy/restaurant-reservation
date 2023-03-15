add_sql = """
INSERT INTO tests.rr_order_items (reservation_id, menu_item_id, count, total_price, comment)
    VALUES(%s,%s,%s,%s,%s);
"""

delete_sql = """
DELETE FROM tests.rr_order_items WHERE menu_item_id = %s
"""

select_sql = """SELECT mi.name as name, mi.category as category, mi.price as price FROM tests.rr_order_items oi
        join tests.rr_menu_items mi on mi.id = oi.menu_item_id"""