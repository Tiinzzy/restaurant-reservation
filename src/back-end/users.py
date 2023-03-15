from database import Database

import users_class_sql as users_table


class Users:
    def __init__(self):
        pass

    @classmethod
    def select_all_roles(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.select_all_users_sql)
        rows = cur.fetchall()
        return rows

    @classmethod
    def insert_into_roles(self, role):
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.insert_in_users_sql, (role,))
        con.commit()
        result = {'count': cur.rowcount}
        db.close_database()
        return result

    @classmethod
    def add(self, user_info):
        data = (user_info['name'],
                user_info['lastName'],
                user_info['email'],
                user_info['password'],
                user_info['birthday'])
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.add_sql, data)
        con.commit()
        result = {'count': cur.rowcount}
        db.close_database()
        return result

    @classmethod
    def delete(self, email):
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.delete_sql, (email,))
        rows = cur.fetchall()
        con.commit()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def load(self, email):
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.load_sql, (email,))
        rows = cur.fetchall()
        result = {}
        if len(rows) == 1:
            result['data_row'] = rows[0]
        db.close_database()
        return result

    @classmethod
    def get_users_role(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.users_role_sql)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({'user_role': row[0]})
        db.close_database()
        return result