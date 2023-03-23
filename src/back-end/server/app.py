from flask import Flask, request, jsonify
from business.user import User
from business.reservation import Reservation

import json
import app_menu_item
import app_seating_table

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
    timestamp = parameters['timestamp']
    customer_name = parameters['customer_name']
    customer_id = parameters['customer_id']
    seat_count = parameters['seat_count']
    table_id = parameters['table_id']
    for_date = parameters['for_date']
    for_how_long = parameters['for_how_long']
    status = parameters['status']
    latest_comment = parameters['latest_comment']
    waiter_id = parameters['waiter_id']
    reservation_type = parameters['reservation_type']
    total_price = parameters['total_price']
    tip_percent = parameters['tip_percent']

    reservation = Reservation()
    reservation.set_timestamp(timestamp)
    reservation.set_customer_name(customer_name)
    reservation.set_customer_id(customer_id)
    reservation.set_seat_count(seat_count)
    reservation.set_table_id(table_id)
    reservation.set_for_date(for_date)
    reservation.set_for_how_long(for_how_long)
    reservation.set_status(status)
    reservation.set_latest_comment(latest_comment)
    reservation.set_waiter_id(waiter_id)
    reservation.set_reservation_type(reservation_type)
    reservation.set_total_price(total_price)
    reservation.set_tip_percent(tip_percent)

    result = reservation.add()
    return jsonify(result)


@app.route('/reservation/all', methods=["POST"])
def get_all_reservations():
    reservations = Reservation.select_all()
    return jsonify(reservations)


@app.route('/reservation/load', methods=["POST"])
def load_a_reservations():
    parameters = get_parameters(request)
    reservation_id = parameters['id']
    reservation = Reservation()
    reservation.load(reservation_id)
    return jsonify(reservation.to_json())


@app.route('/reservation/update', methods=["POST"])
def update_reservations():
    parameters = get_parameters(request)
    reservation_id = parameters['id']
    timestamp = parameters['timestamp']
    customer_name = parameters['customer_name']
    customer_id = parameters['customer_id']
    seat_count = parameters['seat_count']
    table_id = parameters['table_id']
    for_date = parameters['for_date']
    for_how_long = parameters['for_how_long']
    status = parameters['status']
    latest_comment = parameters['latest_comment']
    waiter_id = parameters['waiter_id']
    reservation_type = parameters['reservation_type']
    total_price = parameters['total_price']
    tip_percent = parameters['tip_percent']

    reservation = Reservation()
    reservation.load(reservation_id)

    reservation.set_timestamp(timestamp)
    reservation.set_customer_name(customer_name)
    reservation.set_customer_id(customer_id)
    reservation.set_seat_count(seat_count)
    reservation.set_table_id(table_id)
    reservation.set_for_date(for_date)
    reservation.set_for_how_long(for_how_long)
    reservation.set_status(status)
    reservation.set_latest_comment(latest_comment)
    reservation.set_waiter_id(waiter_id)
    reservation.set_reservation_type(reservation_type)
    reservation.set_total_price(total_price)
    reservation.set_tip_percent(tip_percent)

    result = reservation.update()
    return jsonify(result)


@app.route('/order-item/add', methods=["POST"])
def add_order_item():
    parameters = get_parameters(request)
    reservation_id = parameters['reservation_id']
    menu_item_id = parameters['menu_item_id']
    count = parameters['count']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.add_order_item(menu_item_id, count)
    return jsonify(result)


@app.route('/order-item/all', methods=["POST"])
def select_all_order_items():
    parameters = get_parameters(request)
    reservation_id = parameters['reservation_id']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.select_all_order_items()
    return jsonify(result)


@app.route('/order-item/update', methods=["POST"])
def update_order_item():
    parameters = get_parameters(request)
    reservation_id = parameters['reservation_id']
    order_item_id = parameters['order_item_id']
    count = parameters['count']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.update_order_item(order_item_id, count)
    return jsonify(result)


@app.route('/order-item/delete', methods=["POST"])
def delete_order_item():
    parameters = get_parameters(request)
    reservation_id = parameters['reservation_id']
    menu_item_id = parameters['menu_item_id']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.delete_order_item(menu_item_id)
    return jsonify(result)
