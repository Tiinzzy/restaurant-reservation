add_sql = """
INSERT INTO tests.rr_seating_tables (seat_count, available)
    VALUES (%s,%s);
"""

delete_sql = """
DELETE FROM tests.rr_seating_tables WHERE id = %s ;
"""

select_sql = """
SELECT id FROM tests.rr_seating_tables
    WHERE available = 'True' AND seat_count = %s 
    LIMIT 1;
"""