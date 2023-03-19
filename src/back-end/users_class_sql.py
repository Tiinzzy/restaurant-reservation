select_all_users_sql = """
SELECT * FROM tests.rr_roles;
"""

insert_in_users_sql = """
INSERT INTO tests.rr_roles (name) VALUES (%s);
"""

add_sql = """
INSERT INTO tests.rr_user (name, email, password, birthday) VALUES (%s, %s, %s, %s);
"""

update_sql = """
UPDATE tests.rr_user set name = %s, email = %s, password = %s, birthday = %s WHERE id = %s ;
"""

load_sql = """
SELECT * FROM tests.rr_user WHERE id = %s limit 1;
"""

load_by_email_sql = """
SELECT * FROM tests.rr_user WHERE email = %s limit 1;
"""

select_all_sql = """
SELECT * FROM tests.rr_user WHERE name like %s limit 500;
"""

delete_sql = """
DELETE FROM tests.rr_user WHERE id = %s ;
"""

users_role_sql = """SELECT r.name as role FROM tests.rr_user u
    join tests.rr_user_roles ur on u.id = ur.user_id
    join tests.rr_roles r on r.id = ur.role_id;
"""
