from database import Database
import mysql_tables_class_sql as create_table


class MysqlTables:
    def __init__(self):
        pass

    @classmethod
    def create_roles(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_roles_sql)
        cur.execute(create_table.roles_sql)
        con.commit()
        con.close()

    @classmethod
    def select_roles_count(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_roles_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_user_roles(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_user_roles_sql)
        cur.execute(create_table.user_roles_sql)
        con.commit()
        con.close()

    @classmethod
    def select_user_roles_count(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_user_roles_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_user(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_user_sql)
        cur.execute(create_table.users_sql)
        con.commit()
        con.close()

    @classmethod
    def select_user_count(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_user_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_menu_items(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_menu_sql)
        cur.execute(create_table.menu_sql)
        con.commit()
        con.close()

    @classmethod
    def select_menu_items_count(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_menu_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_order_items(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_order_sql)
        cur.execute(create_table.order_sql)
        con.commit()
        con.close()

    @classmethod
    def select_order_items_count(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_order_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_seating_tables(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_seating_sql)
        cur.execute(create_table.seating_sql)
        con.commit()
        con.close()

    @classmethod
    def select_seating_tables_count(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_seating_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_reservation(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.drop_reservation_sql)
        cur.execute(create_table.reservation_sql)
        con.commit()
        con.close()

    @classmethod
    def select_reservation_count(cls):
        db = Database()
        con, cur = db.open_database()
        cur.execute(create_table.select_reservation_sql)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1
