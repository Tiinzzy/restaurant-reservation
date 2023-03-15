select_all_users_sql = """
SELECT * FROM tests.rr_roles;
"""

insert_in_users_sql = """
INSERT INTO tests.rr_roles (name) VALUES (%s);
"""

add_sql = """
INSERT INTO tests.rr_user (name, lastName, email, password, birthday) VALUES (%s, %s, %s, %s, %s);
"""