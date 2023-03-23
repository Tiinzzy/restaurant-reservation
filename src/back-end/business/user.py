from database import Database
import business.users_class_sql as users_table

ROLES = ['Admin', 'Customer', 'Waiter', 'Cashier']


class User:

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__email = None
        self.__password = None
        self.__birthday = None

    @staticmethod
    def build(name, email, password, birthday):
        user = User()
        user.__name = name
        user.__email = email
        user.__password = password
        user.__birthday = birthday
        return user

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_birthday(self, birthday):
        self.__birthday = birthday

    def get_birthday(self):
        return self.__birthday

    def __is_ok_to_save(self):
        if len(self.__name) < 3 or self.__name is None:
            return False

        if len(self.__email) < 3 or self.__email is None:
            return False

        return True

    def add(self):
        if not self.__is_ok_to_save():
            return False
        data = (self.__name, self.__email, self.__password, self.__birthday)
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.add_sql, data)
        con.commit()
        result = (cur.rowcount == 1)
        self.__id = cur.lastrowid if cur.rowcount == 1 else -1
        db.close_database()
        return result

    def load(self, user_id):
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.load_sql, (user_id,))
        rows = cur.fetchall()
        db.close_database()

        if len(rows) == 1:
            self.__id = rows[0][0]
            self.__name = rows[0][1]
            self.__email = rows[0][2]
            self.__password = rows[0][3]
            self.__birthday = rows[0][4]
            return True
        else:
            return False

    def load_by_email(self, email):
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.load_by_email_sql, (email,))
        rows = cur.fetchall()
        db.close_database()

        if len(rows) == 1:
            self.__id = rows[0][0]
            self.__name = rows[0][1]
            self.__email = rows[0][2]
            self.__password = rows[0][3]
            self.__birthday = rows[0][4]
            return True
        else:
            return False

    def update(self):
        if not self.__is_ok_to_save():
            return False
        data = (self.__name, self.__email, self.__password, self.__birthday, self.__id)
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.update_sql, data)
        con.commit()
        result = (cur.rowcount == 1)
        db.close_database()
        return result

    @staticmethod
    def delete(user_id):
        data = (user_id,)
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.delete_sql, data)
        con.commit()
        result = (cur.rowcount == 1)
        db.close_database()
        return result

    @staticmethod
    def select_all_users(name_filter=""):
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.select_all_sql, ('%' + name_filter + '%',))
        rows = cur.fetchall()
        db.close_database()
        data = []
        for row in rows:
            data.append((row[0], row[1], row[2]))
        return data

    def get_roles(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.select_user_roles_sql, (self.__id,))
        rows = cur.fetchall()
        db.close_database()
        data = []
        for row in rows:
            data.append({'role_id': row[0], 'role': row[1]})
        return data

    def add_role(self, role_name):
        if role_name is None or role_name not in ROLES:
            return False

        data = (self.__id, role_name)
        db = Database()
        con, cur = db.open_database()
        error = None
        try:
            cur.execute(users_table.insert_user_role_sql, data)
            con.commit()
            result = (cur.rowcount == 1)
        except Database.MySqlError as err:
            error = err.msg
            result = False

        db.close_database()
        return result, error

    def delete_role(self, role_name):
        data = (self.__id, role_name)
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.delete_user_role_sql, data)
        con.commit()
        result = (cur.rowcount == 1)
        db.close_database()
        return result

    def to_string(self):
        return str(self.__id) + ', ' + str(self.__name) + ', ' + str(self.__email) + ', ' + str(
            self.__password) + ', ' + self.__birthday

    def to_json(self):
        obj = {'id': self.__id, 'name': self.__name, 'email': self.__email, 'birthday': self.__birthday}
        return obj
