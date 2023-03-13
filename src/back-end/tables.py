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
                name(150)
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
