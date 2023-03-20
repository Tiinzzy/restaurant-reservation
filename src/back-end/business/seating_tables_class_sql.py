add_sql = """
INSERT INTO tests.rr_seating_tables (seat_count, available)
    VALUES (%s,%s);
"""

select_available_sql = """
SELECT id FROM tests.rr_seating_tables
    WHERE available = 'True' AND seat_count = %s ;
"""
update_sql = """
UPDATE tests.rr_seating_tables
    SET available = %s
    WHERE id = %s ; 
"""

delete_sql = """
DELETE FROM tests.rr_seating_tables WHERE id = %s ;
"""
