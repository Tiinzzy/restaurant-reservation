from database import Database


class Users:
    def __init__(self):
        pass

    @classmethod
    def select_all_roles(self):
        db = Database()
        con, cur = db.open_database()
        sql = """SELECT * FROM tests.rr_roles"""
        cur.execute(sql)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({'all_roles': row[0]})
        db.close_database()
        return result

    @classmethod
    def add(self, name, lastName, email, password, birthday):
        db = Database()
        con, cur = db.open_database()
        sql = """INSERT INTO tests.rr_user (name, lastName, email, password, birthday) VALUES (%s, %s, %s, %s, %s)"""
        data = (name, lastName, email, password, birthday)
        cur.execute(sql, data)
        con.commit()
        result = {'count': cur.rowcount}
        db.close_database()
        return result

    @classmethod
    def delete(self, email):
        db = Database()
        con, cur = db.open_database()
        sql = """SELECT  id, name, lastName, email, birthday FROM tests.rr_user WHERE email = '%s'"""
        cur.execute(sql, email)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({'result': row[0]})
        db.close_database()
        return result

    @classmethod
    def load(self, email):
        db = Database()
        con, cur = db.open_database()
        sql = """SELECT * FROM tests.rr_user WHERE email = %s limit 1"""
        cur.execute(sql, (email,))
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
        sql = """SELECT r.name as role FROM tests.rr_user u
                join tests.rr_user_roles ur on u.id = ur.user_id
                join tests.rr_roles r on r.id = ur.role_id"""
        cur.execute(sql)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({'user_role': row[0]})
        db.close_database()
        return result
