from flask import Flask, request, jsonify
from business.user import User
from business.menu_item import MenuItem
from business.seating_table import SeatingTable
from business.reservation import Reservation

import json
import app_menu_item

app = Flask(__name__)


def get_parameters(req):
    return json.loads(req.data.decode('utf8').replace("'", '"'))


@app.route('/create-new-user-account', methods=["POST"])
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


@app.route('/get-menu-items-categories', methods=["POST"])
def get_menu_items_categories():
    categories = MenuItem.get_categories()
    return jsonify(categories)


@app.route('/add-menu-item', methods=["POST"])
def add_menu_item():
    parameters = get_parameters(request)
    name = parameters['name']
    category = parameters['category']
    price = parameters['price']
    description = parameters['description']

    menu_item = MenuItem()
    menu_item.set_name(name)
    menu_item.set_price(price)
    menu_item.set_category(category)
    menu_item.set_description(description)

    result = menu_item.add()
    return jsonify(result)


@app.route('/select-all-menu-items', methods=["POST"])
def select_all_menu_items():
    menu_items = MenuItem.select_all_menu_items()
    return jsonify(menu_items)


@app.route('/delete-menu-item', methods=["POST"])
def delete_menu_item():
    parameters = get_parameters(request)
    menu_item_id = parameters['id']

    menu_item = MenuItem()
    menu_item.load(menu_item_id)

    result = menu_item.delete()
    return jsonify(result)


@app.route('/load-menu-item', methods=["POST"])
def load_menu_item():
    parameters = get_parameters(request)
    menu_item_id = parameters['id']
    menu_item = MenuItem()
    menu_item.load(menu_item_id)
    return jsonify(menu_item.to_json())


@app.route('/menu-item/update', methods=["POST"])
def update_menu_item():
    parameters = get_parameters(request)
    result = app_menu_item.update(parameters)
    return jsonify(result)


@app.route('/seating-table/add', methods=["POST"])
def add_seating_table():
    parameters = get_parameters(request)
    seat_count = parameters['seat_count']
    available = parameters['available']
    if available == 'True':
        available = True
    else:
        available = False

    seating_table = SeatingTable()
    seating_table.set_seat_count(seat_count)
    seating_table.set_available(available)

    result = seating_table.add()
    return jsonify(result)


@app.route('/select-all-available-seats', methods=["POST"])
def select_available_seats():
    seat_count = request.json['seat_count']

    result = SeatingTable.select_available_seats(int(seat_count))
    return jsonify(result)


@app.route('/get-all-seating-tables', methods=["POST"])
def get_all_seating_tables():
    result = SeatingTable.select_all_seating_tables()
    return jsonify(result)


@app.route('/load-seating-table', methods=["POST"])
def load_a_seating_table():
    seat_id = request.json['id']
    table = SeatingTable()
    result = table.load(seat_id)
    return jsonify(result)


@app.route('/update-seating-table', methods=["POST"])
def update_seating_table():
    seat_id = request.json['id']
    available = request.json['available']

    table = SeatingTable()
    table.load(seat_id)
    table.set_available(available)

    result = table.update()
    return jsonify(result)


@app.route('/add-reservation', methods=["POST"])
def add_reservation():
    timestamp = request.json['timestamp']
    customer_name = request.json['customer_name']
    customer_id = request.json['customer_id']
    seat_count = request.json['seat_count']
    table_id = request.json['table_id']
    for_date = request.json['for_date']
    for_how_long = request.json['for_how_long']
    status = request.json['status']
    latest_comment = request.json['latest_comment']
    waiter_id = request.json['waiter_id']
    reservation_type = request.json['reservation_type']
    total_price = request.json['total_price']
    tip_percent = request.json['tip_percent']

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


@app.route('/get-all-reservations', methods=["POST"])
def get_all_reservations():
    reservations = Reservation.select_all()
    return jsonify(reservations)


@app.route('/load-reservation', methods=["POST"])
def load_a_reservations():
    reservation_id = request.json['id']
    reservation = Reservation()

    result = reservation.load(reservation_id)
    return jsonify(result)


@app.route('/update-reservation', methods=["POST"])
def update_reservations():
    reservation_id = request.json['id']
    timestamp = request.json['timestamp']
    customer_name = request.json['customer_name']
    customer_id = request.json['customer_id']
    seat_count = request.json['seat_count']
    table_id = request.json['table_id']
    for_date = request.json['for_date']
    for_how_long = request.json['for_how_long']
    status = request.json['status']
    latest_comment = request.json['latest_comment']
    waiter_id = request.json['waiter_id']
    reservation_type = request.json['reservation_type']
    total_price = request.json['total_price']
    tip_percent = request.json['tip_percent']

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


@app.route('/add-an-order-item', methods=["POST"])
def add_order_item():
    reservation_id = request.json['reservation_id']
    menu_item_id = request.json['menu_item_id']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.add_order_item(menu_item_id)
    return jsonify(result)


@app.route('/select-all-order-items', methods=["POST"])
def select_all_order_items():
    reservation_id = request.json['reservation_id']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.select_all_order_items(reservation_id)
    return jsonify(result)


@app.route('/update-an-order-item', methods=["POST"])
def update_order_item():
    reservation_id = request.json['reservation_id']
    order_item_id = request.json['order_item_id']
    count = request.json['count']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.update_order_item(order_item_id, count)
    return jsonify(result)


@app.route('/delete-order-item', methods=["POST"])
def delete_order_item():
    reservation_id = request.json['reservation_id']
    order_item_id = request.json['order_item_id']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.delete_order_item(order_item_id)
    return jsonify(result)