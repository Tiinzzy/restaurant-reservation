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
                id int,
                name(150)
                )"""
        cur.execute(create_table_sql)
        con.commit()
        con.close()
