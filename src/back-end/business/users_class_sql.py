add_sql = """
INSERT INTO tests.rr_user (name, email, password, birthday) VALUES (%s, %s, %s, %s);
"""

load_sql = """
SELECT * FROM tests.rr_user WHERE id = %s limit 1;
"""

load_by_email_sql = """
SELECT * FROM tests.rr_user WHERE email = %s limit 1;
"""

update_sql = """
UPDATE tests.rr_user set name = %s, email = %s, password = %s, birthday = %s WHERE id = %s;
"""

delete_sql = """
DELETE FROM tests.rr_user WHERE id = %s;
"""

select_all_sql = """
SELECT * FROM tests.rr_user WHERE name like %s order by id limit 500;
"""

select_user_roles_sql = """
SELECT r.id, r.name as role FROM tests.rr_user u
join tests.rr_user_roles ur on u.id = ur.user_id
join tests.rr_roles r on r.id = ur.role_id
WHERE u.id = %s;
"""

insert_user_role_sql = """
INSERT INTO tests.rr_user_roles (user_id, role_id) 
VALUES (%s, (SELECT id FROM tests.rr_roles r WHERE r.name = %s))
"""

delete_user_role_sql = """
DELETE FROM tests.rr_user_roles WHERE user_id = %s AND role_id = (SELECT id FROM tests.rr_roles r WHERE r.name = %s)
"""

# Queries we don't use in new implementation


select_all_users_sql = """
SELECT * FROM tests.rr_roles;
"""
