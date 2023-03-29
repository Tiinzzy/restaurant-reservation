from datetime import datetime
from database import Database


session_storage = {}


def __get_user_session(username):
    timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    if username in session_storage.keys():
        session_storage[username]['last_check_time'] = session_storage[username]['login_time']
        session_storage[username]['login_time'] = timestamp
    else:
        session_storage[username] = {'login_time': timestamp, 'last_check_time': None}
    return session_storage[username]


def login(session, params):
    username = params.get('user')
    password = params.get('password')
    success = valid_user(username, password)
    if success:
        session[username] = __get_user_session(username)
        print(session[username])
    return {'success': success}


def logout(session, params):
    username = params.get('username')
    session.pop(username, None)
    return {'success': True}


def is_login(session, params):
    username = params.get('user')
    result = username in session
    if result:
        print(session[username])
    return {'is_login': result, 'user': username}


def valid_user(username, password):
    sql = 'SELECT password FROM tests.rr_user WHERE email = %s ;'

    db = Database()
    con, cur = db.open_database()
    cur.execute(sql, (username,))
    rows = cur.fetchall()
    db_password = rows[0][0]
    if db_password == password:
        result = True
    else:
        result = False
    return result
