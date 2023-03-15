add_sql = """
INSERT INTO tests.rr_seating_tables (seat_count, available)
    VALUES (%s,%s)
"""