from business.user import User


def add(parameters):
    name = parameters.get('name')
    email = parameters.get('email')
    password = parameters.get('password')
    birthday = parameters.get('birthday')

    user = User()
    user.set_name(name)
    user.set_email(email)
    user.set_password(password)
    user.set_birthday(birthday)

    result = user.add()
    return {'result': result}


def select_all(parameters):
    name = parameters.get('name')
    users = User.select_all_users(name)
    return users


def load(parameters):
    user_id = parameters.get('user_id')
    user = User()
    user.load(user_id)
    return user.to_json()


def load_by_email(parameters):
    email = parameters.get('email')
    user = User()
    user.load_by_email(email)
    return user.to_json()


def update(parameters):
    user_id = parameters.get('user_id')
    name = parameters.get('name')
    email = parameters.get('email')
    password = parameters.get('password')
    birthday = parameters.get('birthday')

    user = User()
    user.load(user_id)

    user.set_name(name)
    user.set_email(email)
    user.set_password(password)
    user.set_birthday(birthday)
    result = user.update()
    return {'result': result}


def delete(parameters):
    user_id = parameters.get('user_id')
    result = User.delete(user_id)
    return {'result': result}


def get_roles(parameters):
    user_id = parameters.get('user_id')
    user = User()
    user.load(user_id)
    result = user.get_roles()
    return result


def add_role(parameters):
    user_id = parameters.get('user_id')
    role_name = parameters.get('role_name')
    user = User()
    user.load(user_id)
    result = user.add_role(role_name)
    return {'result': result}


def delete_role(parameters):
    user_id = parameters.get('user_id')
    role_name = parameters.get('role_name')
    user = User()
    user.load(user_id)
    result = user.delete_role(role_name)
    return {'result': result}
