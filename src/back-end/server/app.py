from flask import Flask, request, jsonify, session

import json
import app_menu_item
import app_seating_table
import app_reservation
import app_user
import app_authentication

app = Flask(__name__)
app.secret_key = 'hello world, this encrypts my sessions'


def get_parameters(req):
    return json.loads(req.data.decode('utf8').replace("'", '"'))


@app.route('/user/add', methods=["POST"])
def user_add():
    parameters = get_parameters(request)
    result = app_user.add(parameters)
    return jsonify(result)


@app.route('/user/all', methods=["POST"])
def user_all():
    parameters = get_parameters(request)
    result = app_user.select_all(parameters)
    return jsonify(result)


@app.route('/user/load', methods=["POST"])
def user_load():
    parameters = get_parameters(request)
    result = app_user.load(parameters)
    return jsonify(result)


@app.route('/user/load-by-email', methods=["POST"])
def user_load_by_email():
    parameters = get_parameters(request)
    result = app_user.load_by_email(parameters)
    return jsonify(result)


@app.route('/user/update', methods=["POST"])
def user_update():
    parameters = get_parameters(request)
    result = app_user.update(parameters)
    return jsonify(result)


@app.route('/user/delete', methods=["POST"])
def user_delete():
    parameters = get_parameters(request)
    result = app_user.delete(parameters)
    return jsonify(result)


@app.route('/user/get-roles', methods=["POST"])
def user_get_roles():
    parameters = get_parameters(request)
    result = app_user.get_roles(parameters)
    return jsonify(result)


@app.route('/user/add-role', methods=["POST"])
def user_add_role():
    parameters = get_parameters(request)
    result = app_user.add_role(parameters)
    return jsonify(result)


@app.route('/user/delete-role', methods=["POST"])
def user_delete_role():
    parameters = get_parameters(request)
    result = app_user.delete_role(parameters)
    return jsonify(result)


@app.route('/menu-item/categories', methods=["POST"])
def menu_items_categories():
    categories = app_menu_item.categories()
    return jsonify(categories)


@app.route('/menu-item/add', methods=["POST"])
def menu_item_add():
    parameters = get_parameters(request)
    result = app_menu_item.add(parameters)
    return jsonify(result)


@app.route('/menu-item/all', methods=["POST"])
def menu_item_all():
    result = app_menu_item.select_all()
    return jsonify(result)


@app.route('/menu-item/delete', methods=["POST"])
def menu_item_delete():
    parameters = get_parameters(request)
    result = app_menu_item.delete(parameters)
    return jsonify(result)


@app.route('/menu-item/load', methods=["POST"])
def menu_item_load():
    parameters = get_parameters(request)
    result = app_menu_item.load(parameters)
    return jsonify(result)


@app.route('/menu-item/update', methods=["POST"])
def menu_item_update():
    parameters = get_parameters(request)
    result = app_menu_item.update(parameters)
    return jsonify(result)

@app.route('/menu-item/truncate', methods=["POST"])
def menu_item_truncate():
    result = app_menu_item.truncate()
    return jsonify(result)    


@app.route('/seating-table/add', methods=["POST"])
def seating_table_add():
    parameters = get_parameters(request)
    result = app_seating_table.add(parameters)
    return jsonify(result)


@app.route('/seating-table/available-seats', methods=["POST"])
def seating_table_available_seats():
    parameters = get_parameters(request)
    result = app_seating_table.available_seats(parameters)
    return jsonify(result)


@app.route('/seating-table/all', methods=["POST"])
def seating_table_all():
    result = app_seating_table.select_all()
    return jsonify(result)


@app.route('/seating-table/load', methods=["POST"])
def seating_table_load():
    parameters = get_parameters(request)
    result = app_seating_table.load(parameters)
    return jsonify(result)


@app.route('/seating-table/update', methods=["POST"])
def seating_table_update():
    parameters = get_parameters(request)
    result = app_seating_table.update(parameters)
    return jsonify(result)


@app.route('/reservation/add', methods=["POST"])
def reservation_add():
    parameters = get_parameters(request)
    result = app_reservation.add(parameters)
    return jsonify(result)


@app.route('/reservation/all', methods=["POST"])
def reservation_all():
    result = app_reservation.select_all()
    return jsonify(result)


@app.route('/reservation/load', methods=["POST"])
def reservation_load():
    parameters = get_parameters(request)
    result = app_reservation.load(parameters)
    return result


@app.route('/reservation/update', methods=["POST"])
def reservations_update():
    parameters = get_parameters(request)
    result = app_reservation.update(parameters)
    return jsonify(result)


@app.route('/order-item/add', methods=["POST"])
def order_item_add():
    parameters = get_parameters(request)
    result = app_reservation.add_order_item(parameters)
    return jsonify(result)


@app.route('/order-item/all', methods=["POST"])
def order_item_all():
    parameters = get_parameters(request)
    result = app_reservation.select_all_order_items(parameters)
    return jsonify(result)


@app.route('/order-item/update', methods=["POST"])
def order_item_update():
    parameters = get_parameters(request)
    result = app_reservation.update_order_item(parameters)
    return jsonify(result)


@app.route('/order-item/delete', methods=["POST"])
def order_item_delete():
    parameters = get_parameters(request)
    result = app_reservation.delete_order_item(parameters)
    return jsonify(result)


@app.route('/authentication/login', methods=["POST"])
def login():
    parameters = get_parameters(request)
    result = app_authentication.login(session, parameters)
    return jsonify(result)


@app.route('/authentication/logout', methods=["POST"])
def logout():
    parameters = get_parameters(request)
    result = app_authentication.logout(session, parameters)
    return jsonify(result)


@app.route('/authentication/is_login', methods=["POST"])
def is_login():
    parameters = get_parameters(request)
    result = app_authentication.is_login(session, parameters)
    return jsonify(result)
