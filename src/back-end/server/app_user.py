from business.user import User


def add(parameters):
    name = parameters['name']
    email = parameters['email']
    password = parameters['password']
    birthday = parameters['birthday']

    user = User()
    user.set_name(name)
    user.set_email(email)
    user.set_password(password)
    user.set_birthday(birthday)

    result = user.add()
    return result


def select_all(parameters):
    name = parameters['name']
    users = User.select_all_users(name)
    return users


def load(parameters):
    user_id = parameters['user_id']
    user = User()
    user.load(user_id)
    return user.to_json()


def load_by_email(parameters):
    email = parameters['email']
    user = User()
    user.load_by_email(email)
    return user.to_json()


def update(parameters):
    user_id = parameters['user_id']
    name = parameters['name']
    email = parameters['email']
    password = parameters['password']
    birthday = parameters['birthday']

    user = User()
    user.load(user_id)

    user.set_name(name)
    user.set_email(email)
    user.set_password(password)
    user.set_birthday(birthday)
    result = user.update()
    if result:
        value = {'result': 'True'}
    else:
        value = {'result': 'False'}
    return value


def delete(parameters):
    user_id = parameters['user_id']
    result = User.delete(user_id)
    if result:
        value = {'result': 'True'}
    else:
        value = {'result': 'False'}
    return value


def get_roles(parameters):
    user_id = parameters['user_id']
    user = User()
    user.load(user_id)
    result = user.get_roles()
    return result


def add_role(parameters):
    user_id = parameters['user_id']
    role_name = parameters['role_name']
    user = User()
    user.load(user_id)
    result = user.add_role(role_name)
    if result:
        value = {'result': 'True'}
    else:
        value = {'result': 'False'}
    return value


def delete_role(parameters):
    user_id = parameters['user_id']
    role_name = parameters['role_name']
    user = User()
    user.load(user_id)
    result = user.delete_role(role_name)
    if result:
        value = {'result': 'True'}
    else:
        value = {'result': 'False'}
    return value
