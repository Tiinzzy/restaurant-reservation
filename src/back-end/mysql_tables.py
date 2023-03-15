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
        cur.execute(create_table.drop_roles_sql)
        cur.execute(create_table.roles_sql)
        con.commit()
        con.close()

    @classmethod
    def select_roles_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_roles_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_user_roles(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_user_roles_sql)
        cur.execute(create_table.user_roles_sql)
        con.commit()
        con.close()

    @classmethod
    def select_user_roles_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_user_roles_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_user(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_user_sql)
        cur.execute(create_table.users_sql)
        con.commit()
        con.close()

    @classmethod
    def select_user_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_user_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_menu_items(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_menu_sql)
        cur.execute(create_table.menu_sql)
        con.commit()
        con.close()

    @classmethod
    def select_menu_items_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_menu_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_order_items(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_order_sql)
        cur.execute(create_table.order_sql)
        con.commit()
        con.close()

    @classmethod
    def select_order_items_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_order_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_seating_tables(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_seating_sql)
        cur.execute(create_table.seating_sql)
        con.commit()
        con.close()

    @classmethod
    def select_seating_tables_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_seating_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_reservation(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_reservation_sql)
        cur.execute(create_table.reservation_sql)
        con.commit()
        con.close()

    @classmethod
    def select_reservation_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.reservation_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1
