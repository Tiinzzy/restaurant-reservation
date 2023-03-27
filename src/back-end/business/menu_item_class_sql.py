add_sql = """
INSERT INTO tests.rr_menu_items (name, category, price, description)
    VALUES(%s,%s,%s,%s);
"""

delete_sql = """
DELETE FROM tests.rr_menu_items WHERE id = %s ; 
"""

select_all_sql = """
select * from tests.rr_menu_items order by id limit 500;
"""

laod_sql = """
SELECT * FROM tests.rr_menu_items WHERE id = %s ; 
"""

update_sql = """
UPDATE tests.rr_menu_items SET name = %s , category = %s , price = %s , description = %s 
WHERE id = %s;
"""

truncate_sql = """
TRUNCATE TABLE tests.rr_menu_items;
"""