add_sql = """
INSERT INTO tests.rr_seating_tables (seat_count, available)
    VALUES (%s,%s);
"""

delete_sql = """
DELETE FROM tests.rr_seating_tables WHERE id = %s ;
"""
