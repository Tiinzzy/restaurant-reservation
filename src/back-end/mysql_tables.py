from database import Database
import create_tables_sql as create_table

def read_sql_file(sql_filename):
    file = open("sql/"+sql_filename, "r")
    content = file.read()
    file.close()
    return content


class MysqlTables:
    def __init__(self):
        pass

    @classmethod
    def create_roles(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('drop_roles.sql'))
        cur.execute(create_table.roles_sql)
        con.commit()
        con.close()

    @classmethod
    def select_roles_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('select_roles_count.sql'))
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_user_roles(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('drop_user_roles.sql'))
        cur.execute(read_sql_file('create_user_roles.sql'))
        con.commit()
        con.close()

    @classmethod
    def select_user_roles_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('select_user_roles_count.sql'))
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_user(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('drop_user.sql'))
        cur.execute(read_sql_file('create_user.sql'))
        con.commit()
        con.close()

    @classmethod
    def select_user_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('select_user_count.sql'))
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_menu_items(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('drop_menu_items.sql'))
        cur.execute(read_sql_file('create_menu_items.sql'))
        con.commit()
        con.close()

    @classmethod
    def select_menu_items_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('select_menu_items_count.sql'))
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_order_items(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('drop_order_items.sql'))
        cur.execute(read_sql_file('create_order_items.sql'))
        con.commit()
        con.close()

    @classmethod
    def select_order_items_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('select_order_items_count.sql'))
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_seating_tables(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('drop_seating_tables.sql'))
        cur.execute(read_sql_file('create_seating_tables.sql'))
        con.commit()
        con.close()

    @classmethod
    def select_seating_tables_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('select_seating_tables_count.sql'))
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_reservation(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('drop_reservation.sql'))
        cur.execute(read_sql_file('create_reservation.sql'))
        con.commit()
        con.close()

    @classmethod
    def select_reservation_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(read_sql_file('select_reservation_count.sql'))
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1
