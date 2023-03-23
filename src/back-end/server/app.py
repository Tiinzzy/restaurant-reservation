from flask import Flask, request, jsonify
from business.user import User

import json
import app_menu_item
import app_seating_table
import app_reservation

app = Flask(__name__)


def get_parameters(req):
    return json.loads(req.data.decode('utf8').replace("'", '"'))


@app.route('/user/add', methods=["POST"])
def create_new_user():
    parameters = get_parameters(request)
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
    return jsonify(result)


@app.route('/get-all-user-roles', methods=["POST"])
def get_all_user_roles():
    pass


@app.route('/update-user-account', methods=["POST"])
def update_user_account():
    pass


@app.route('/delete-users-role', methods=["POST"])
def delete_user_roles():
    pass


@app.route('/add-user-role', methods=["POST"])
def add_user_role():
    pass


@app.route('/menu-items/categories', methods=["POST"])
def get_menu_items_categories():
    categories = app_menu_item.categories()
    return jsonify(categories)


@app.route('/menu-item/add', methods=["POST"])
def add_menu_item():
    parameters = get_parameters(request)
    result = app_menu_item.add(parameters)
    return jsonify(result)


@app.route('/menu-item/all', methods=["POST"])
def select_all_menu_items():
    result = app_menu_item.select_all()
    return jsonify(result)


@app.route('/menu-item/delete', methods=["POST"])
def delete_menu_item():
    parameters = get_parameters(request)
    result = app_menu_item.delete(parameters)
    return jsonify(result)


@app.route('/menu-item/load', methods=["POST"])
def load_menu_item():
    parameters = get_parameters(request)
    result = app_menu_item.load(parameters)
    return jsonify(result)


@app.route('/menu-item/update', methods=["POST"])
def update_menu_item():
    parameters = get_parameters(request)
    result = app_menu_item.update(parameters)
    return jsonify(result)


@app.route('/seating-table/add', methods=["POST"])
def add_seating_table():
    parameters = get_parameters(request)
    result = app_seating_table.add(parameters)
    return jsonify(result)


@app.route('/seating-table/available-seats', methods=["POST"])
def select_available_seats():
    parameters = get_parameters(request)
    result = app_seating_table.available_seats(parameters)
    return jsonify(result)


@app.route('/seating-table/all', methods=["POST"])
def get_all_seating_tables():
    result = app_seating_table.select_all()
    return jsonify(result)


@app.route('/seating-table/load', methods=["POST"])
def load_a_seating_table():
    parameters = get_parameters(request)
    result = app_seating_table.load(parameters)
    return jsonify(result)


@app.route('/seating-table/update', methods=["POST"])
def update_seating_table():
    parameters = get_parameters(request)
    result = app_seating_table.update(parameters)
    return jsonify(result)


@app.route('/reservation/add', methods=["POST"])
def add_reservation():
    parameters = get_parameters(request)
    result = app_reservation.add(parameters)
    return jsonify(result)


@app.route('/reservation/all', methods=["POST"])
def get_all_reservations():
    result = app_reservation.select_all()
    return jsonify(result)


@app.route('/reservation/load', methods=["POST"])
def load_a_reservations():
    parameters = get_parameters(request)
    result = app_reservation.load(parameters)
    return result


@app.route('/reservation/update', methods=["POST"])
def update_reservations():
    parameters = get_parameters(request)
    result = app_reservation.update(parameters)
    return jsonify(result)


@app.route('/order-item/add', methods=["POST"])
def add_order_item():
    parameters = get_parameters(request)
    result = app_reservation.add_order_item(parameters)
    return jsonify(result)


@app.route('/order-item/all', methods=["POST"])
def select_all_order_items():
    parameters = get_parameters(request)
    result = app_reservation.select_all_order_items(parameters)
    return jsonify(result)


@app.route('/order-item/update', methods=["POST"])
def update_order_item():
    parameters = get_parameters(request)
    result = app_reservation.update_order_item(parameters)
    return jsonify(result)


@app.route('/order-item/delete', methods=["POST"])
def delete_order_item():
    parameters = get_parameters(request)
    result = app_reservation.delete_order_item(parameters)
    return jsonify(result)
