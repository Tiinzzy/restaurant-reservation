add_sql = """
INSERT INTO tests.rr_menu_items (name, category, price, description)
    VALUES(%s,%s,%s,%s);
"""

delete_sql = """
DELETE FROM tests.rr_menu_items WHERE id = %s ; 
"""
