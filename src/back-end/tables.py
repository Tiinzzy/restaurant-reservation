from database import Database


class Tables:
    def __init__(self):
        pass

    @classmethod
    def create_roles(self):
        db = Database()
        con, cur = db.open_database()
        cur.execute("drop table if exists tests.rr_roles")
        create_table_sql = """
        create table tests.rr_roles (
                id int NOT NULL AUTO_INCREMENT,
                name varchar(100),
                PRIMARY KEY (id)
                )"""
        cur.execute(create_table_sql)
        con.commit()
        con.close()

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
