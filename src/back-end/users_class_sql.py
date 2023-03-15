select_all_users_sql = """
SELECT * FROM tests.rr_roles;
"""

insert_in_users_sql = """
INSERT INTO tests.rr_roles (name) VALUES (%s);
"""