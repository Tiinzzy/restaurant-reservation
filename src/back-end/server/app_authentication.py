from datetime import datetime
from database import Database
import business.users_class_sql as users_table

import uuid

session_storage = {}
session_id_to_user_name = {}
user_role_storage = {}


def __get_user_session(username):
    session_id = str(uuid.uuid4())
    session_id_to_user_name[session_id] = username
    timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    if username in session_storage.keys():
        session_storage[username]['last_check_time'] = session_storage[username]['login_time']
        session_storage[username]['login_time'] = timestamp
        session_storage[username]['session_id'] = session_id
    else:
        session_storage[username] = {'login_time': timestamp, 'last_check_time': None, 'session_id': session_id}
    return session_storage[username]


def login(session, params):
    username = params.get('user')
    password = params.get('password')
    user_id = params.get('user_id')
    success = valid_user(username, password)
    roles = []
    session_id = None
    if success:
        session[username] = __get_user_session(username)
        session_id = session[username]['session_id']
        roles = get_user_roles(user_id, username)
    return {'success': success, 'roles': roles, 'session_id': session_id}


def get_user_roles(user_id, username):
    if username in user_role_storage:
        return user_role_storage[username]
    else:
        db = Database()
        con, cur = db.open_database()
        cur.execute(users_table.select_user_roles_sql, (int(user_id),))
        rows = cur.fetchall()
        db.close_database()
        data = []
        for row in rows:
            data.append({'role_id': row[0], 'role': row[1]})
        user_role_storage[username] = data[0]['role']
    return user_role_storage[username]


def logout(session, params):
    session_id = params.get('session_id')
    session.pop(session_id_to_user_name[session_id], None)
    del session_id_to_user_name[session_id]
    return {'success': True}


def is_login(params):
    session_id = params.get('session_id')
    result = False
    roles = []
    username = None
    if session_id in session_id_to_user_name.keys():
        result = True
        username = session_id_to_user_name[session_id]
        roles = user_role_storage[username]
    return {'is_login': result, 'user': username, 'roles': roles, 'session_id': session_id}


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
