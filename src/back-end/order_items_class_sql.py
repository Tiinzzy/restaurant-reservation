add_sql = """
INSERT INTO tests.rr_order_items (reservation_id, menu_item_id, count, total_price, comment)
    VALUES(%s,%s,%s,%s,%s);
"""