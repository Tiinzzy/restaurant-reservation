from database import Database

SELECT_ROLE_TABLE_COUNT_SQL = "SELECT COUNT(*) FROM tests.rr_roles"


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
        cur.execute(read_sql_file('create_roles.sql'))
        con.commit()
        con.close()

    @classmethod
    def select_roles_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(SELECT_ROLE_TABLE_COUNT_SQL)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_user_roles(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute("drop table if exists tests.rr_user_roles")
        create_table_sql = """
        create tests.rr_user_roles (
                user_id int,
                role_id int
                )"""
        cur.execute(create_table_sql)
        con.commit()
        con.close()

    @classmethod
    def select_user_roles_count(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute(SELECT_ROLE_TABLE_COUNT_SQL)
        rows = cur.fetchall()
        con.close()
        return rows[0][0] if rows is not None and len(rows) == 1 else -1

    @classmethod
    def create_user(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute("drop table if exists tests.rr_user")
        create_table_sql = """
        create tests.rr_user (
                id int NOT NULL AUTO_INCREMENT,
                name varchar(200),
                lastName varchar(200),
                email varchar(200),
                password varchar(200),
                birthday varchar(200),
                PRIMARY KEY (id)
                )"""
        cur.execute(create_table_sql)
        con.commit()
        con.close()

    @classmethod
    def create_menu_items(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute("drop table if exists tests.rr_menu_items")
        create_table_sql = """
        create tests.rr_menu_items (
                id int NOT NULL AUTO_INCREMENT,
                name varchar(200),
                category varchar(200),
                price int,
                description varchar(200),
                PRIMARY KEY (id)
                )"""
        cur.execute(create_table_sql)
        con.commit()
        con.close()

    @classmethod
    def create_order_items(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute("drop table if exists tests.rr_order_items")
        create_table_sql = """
        create tests.rr_order_items (
                id int NOT NULL AUTO_INCREMENT,
                reservation_id int,
                menu_item_id int,
                count int,
                total_price int,
                comment varchar(200)
                )"""
        cur.execute(create_table_sql)
        con.commit()
        con.close()

    @classmethod
    def create_tables(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute("drop table if exists tests.rr_tables")
        create_table_sql = """
        create tests.rr_tables (
                id int NOT NULL AUTO_INCREMENT,
                seat_count int,
                available varchar(20),
                PRIMARY KEY (id)
                )"""
        cur.execute(create_table_sql)
        con.commit()
        con.close()

    @classmethod
    def create_reservation(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute("drop table if exists tests.rr_reservation")
        create_table_sql = """
        create tests.rr_reservation (
                id int NOT NULL AUTO_INCREMENT,
                timestamp varchar(100),
                customer_name varchar(20),
                customer_id int,
                name varchar(20),
                seat_count int,
                table_id int,
                for_date varchar(100),
                for_how_long varchar(100),
                status varchar(100),
                latest_comment varchar(100),
                waiter_id int,
                total_price int,
                tip_percent int
                PRIMARY KEY (id)
                )"""
        cur.execute(create_table_sql)
        con.commit()
        con.close()
