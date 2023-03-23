from flask import Flask, request, jsonify

import json
import app_menu_item
import app_seating_table
import app_reservation
import app_user

app = Flask(__name__)


def get_parameters(req):
    return json.loads(req.data.decode('utf8').replace("'", '"'))


@app.route('/user/add', methods=["POST"])
def create_new_user():
    parameters = get_parameters(request)
    result = app_user.add(parameters)
    return jsonify(result)


@app.route('/user/all', methods=["POST"])
def get_all_users():
    parameters = get_parameters(request)
    result = app_user.select_all(parameters)
    return result


@app.route('/user/load', methods=["POST"])
def load_user_account():
    parameters = get_parameters(request)
    result = app_user.load(parameters)
    return result


@app.route('/user/load-by-email', methods=["POST"])
def load_user_account_by_email():
    parameters = get_parameters(request)
    result = app_user.load_by_email(parameters)
    return result


@app.route('/user/update', methods=["POST"])
def update_user_account():
    parameters = get_parameters(request)
    result = app_user.update(parameters)
    return result


@app.route('/user/delete', methods=["POST"])
def delete_user_account():
    parameters = get_parameters(request)
    result = app_user.delete(parameters)
    return result


@app.route('/user/get-roles', methods=["POST"])
def get_users_roles():
    parameters = get_parameters(request)
    result = app_user.get_roles(parameters)
    return result


@app.route('/user/add-role', methods=["POST"])
def add_users_roles():
    parameters = get_parameters(request)
    result = app_user.add_role(parameters)
    return result


@app.route('/user/delete-role', methods=["POST"])
def delete_users_roles():
    parameters = get_parameters(request)
    result = app_user.delete_role(parameters)
    return result


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
